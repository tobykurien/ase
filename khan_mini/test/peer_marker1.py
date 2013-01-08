import pycurl
import cStringIO
from urllib import urlencode
import re
 
SERVER = "http://localhost:8081"


def makeCurlObject():
    c = pycurl.Curl()
    c.setopt(pycurl.COOKIEFILE, 'cookie.txt')
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    return c

def sendRequest(curlObject, path, postfields=""):
    buf = cStringIO.StringIO()
    c = curlObject
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.setopt(c.URL, SERVER+path)
    c.setopt(c.POSTFIELDS, postfields)
    result = c.perform()
    result =  buf.getvalue()
    buf.close()
    return result


def testPage(curlObject, path, expectedText, message, postfields=""):
    result = sendRequest(curlObject, path, postfields)
    if result.find(expectedText )==-1:
       print result
       raise Exception(message)
    return result

def testPageRex(curlObject, path, expectedRE, message, postfields=""):
    result = sendRequest(curlObject, path, postfields)
    if re.search(expectedRE, result) == None:
       print result
       raise Exception(message)
    return result

#student
student1 = makeCurlObject()     
testPage(student1,'/login', "<title>Menu - KhanAcademy</title>","Login failed", 'username=s1')
testPage(student1,'/englishessay/', "Here is a list of your previous assignments","EnglishEssay failed")

#teacher
admin = makeCurlObject() 
testPage(admin,'/englishessay/admin', "<title>Assignments - KhanAcademy</title>","Admin login failed", 'password=x')

newass = {'assignmentid':'new','oper':'add','title':'My holiday','description':'My holiday','duration':'15'}
testPage(admin,'/englishessay/admineditassignment', "My holiday","New assignment failed", urlencode(newass))

# teacher activates essay
testPage(admin,'/englishessay/adminopassignment?assignmentid=1&oper=busy', """<button onclick="javascript:document.location='adminopassignment?assignmentid=1&oper=marking'">Mark</button>""","Set to busy failed")

# student1 sees and submits an essay
testPage(student1,'/englishessay/', '''<form action="submitAssignment" method="post">''',"EnglishEssay not ready for submission")
s1ass = {'assignmentid':'1','essay_text':'Student 1 essay','bsubmit':'Save'}
testPage(student1, '/englishessay/submitAssignment',"","Submitting assignment failed", urlencode(s1ass))

# student 2 sees and submits an essay
student2 = makeCurlObject()     
testPage(student2,'/login', "<title>Menu - KhanAcademy</title>","Login failed", 'username=s2')
s2ass = {'assignmentid':'1','essay_text':'Student 2 essay','bsubmit':'Save'}
testPage(student2, '/englishessay/submitAssignment',"","Submitting assignment failed", urlencode(s2ass))

# student 3 sees and submits an essay
student3 = makeCurlObject()     
testPage(student3,'/login', "<title>Menu - KhanAcademy</title>","Login failed", 'username=s3')
s3ass = {'assignmentid':'1','essay_text':'Student 3 essay','bsubmit':'Save'}
testPage(student3, '/englishessay/submitAssignment',"","Submitting assignment failed", urlencode(s3ass))

# teacher sees the submitted essays
testPage(admin, '/englishessay/adminessayresults?assignmentid=1&complete=0', '<td>Student 1 essay', 'Student essay missing')

# teacher set marking mode
testPage(admin,'/englishessay/adminopassignment?assignmentid=1&oper=marking', """<button class="btn" onclick="javascript:document.location='adminopassignment?assignmentid=1&oper=complete'">Complete</button>""","Set to marking failed")

for i,student in enumerate([student1, student2, student3]):
    studentid = str(i+1)
    # s1 marks
    result = testPage(student,'/englishessay/', '''Student Marking: s%s''' % studentid,"EnglishEssay not ready for marking for s%s" % studentid)
    # check that student does not get own essay
    if result.find("Student %s essay" % studentid) != -1:
      raise Exception("Student %s got own essay to mark" % studentid)
    m = re.search("""<input type="hidden" name="essay1_id" value="(\d+)"/>""", result)
    essay1 = m.groups()[0]
    m = re.search("""<input type="hidden" name="essay2_id" value="(\d+)"/>""", result)    
    essay2 = m.groups()[0]
    m = re.search("""<input type="hidden" name="essayeval_id" value="(\d+)"/>""", result)    
    essayevalid = m.groups()[0]
    
    s1mark = {'essayeval_id':essayevalid,'essay1_id':str(essay1),'essay2_id':str(essay2), 'scorerange':'0.0','pcomment1':'pcomment%s'% essay1,'ccomment1':'ccomment%s'%essay1,'ccomment2':'ccomment%s'%essay2,'pcomment2':'pcomment%s'%essay2,'bsubmit':'Next >','pcountdown1':'0','pcountdown2':'0','ccountdown1':'0','ccountdown2':'0'}
    testPage(student, '/englishessay/evalEssay',"s%s - Done marking" % studentid,"Submitting marking failed", urlencode(s1mark))

# teacher set marking mode
testPage(admin,'/englishessay/adminopassignment?assignmentid=1&oper=complete', """<button class="btn" onclick="document.location='adminessayresults?assignmentid=1&complete=1'">View</button> ""","Set to complete failed")

# Student view result before grading
for i,student in enumerate([student1, student2, student3]):
    studentid = str(i+1)
    testPageRex(student,'/englishessay/', '''<td>None</td>([^<]*)<td>Student %s''' % studentid,"Student essay not correct after marking s%s" % studentid)
    testPage(student, '/englishessay/viewessay?essayid=%s' % studentid,"<b>Grade</b> : None<br/>","Submitting view essay mark failed")

## teacher grades
calcmarks = {"lowgrade":40, "highgrade":80, "assignmentid":1}
testPage(admin,'/englishessay/adminsubmitmarks', """<td>80.0</td>""","Set to complete failed", urlencode(calcmarks))







print "Tests done"
