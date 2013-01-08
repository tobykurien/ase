import pycurl
import cStringIO
from urllib import urlencode
import re
import math
 
SERVER = "http://localhost:8081"


def makeCurlObject():
    c = pycurl.Curl()
    c.setopt(pycurl.COOKIEFILE, 'cookie.txt')
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    return c

def sendRequest(curlObject, path, postfields=""):
    print "in sendRequest"
    buf = cStringIO.StringIO()
    c = curlObject
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.setopt(c.URL, SERVER+path)
    c.setopt(c.POSTFIELDS, postfields)
    print "before sending"
    result = c.perform()
    print "after sending"
    result =  buf.getvalue()
    buf.close()
    return result


def testPage(curlObject, path, expectedText, message, postfields=""):
    print "Testing for .....",expectedText," path = ",path,
    result = sendRequest(curlObject, path, postfields)
    if result.find(expectedText )==-1:
       print result
       print "expectedText:",expectedText
       raise Exception(message)
    print "PASSED"   
    return result

def testPageRex(curlObject, path, expectedRE, message, postfields=""):
    print "Testing for .....",expectedRE," path = ",path,
    result = sendRequest(curlObject, path, postfields)
    if re.search(expectedRE, result) == None:
       print result
       raise Exception(message)
    print "PASSED"       
    return result


NumberOfStudents = 5
studentArr = [makeCurlObject() for i in range(NumberOfStudents)]
#student
for i,student in enumerate(studentArr):
    studentid = str(i+1)
    testPage(student,'/login', "<title>Menu - KhanAcademy</title>","Login failed", 'username=s%s'%studentid)
    testPage(student,'/englishessay/', "Here is a list of your previous assignments","EnglishEssay failed")

#teacher
admin = makeCurlObject() 
testPage(admin,'/englishessay/admin', "<title>Assignments - KhanAcademy</title>","Admin login failed", 'password=x')

newass = {'assignmentid':'new','oper':'add','title':'My holiday','description':'My holiday','duration':'15'}
testPage(admin,'/englishessay/admineditassignment', "My holiday","New assignment failed", urlencode(newass))

# teacher activates essay
testPage(admin,'/englishessay/adminopassignment?assignmentid=1&oper=busy', """<button onclick="javascript:document.location='adminopassignment?assignmentid=1&oper=marking'">Mark</button>""","Set to busy failed")

# student sees and submits an essay
for i,student in enumerate(studentArr):
    studentid = str(i+1)
    testPage(student,'/englishessay/', '''<form action="submitAssignment" method="post">''',"EnglishEssay not ready for submission")
    s1ass = {'assignmentid':'1','essay_text':'Student %s essay' % studentid,'bsubmit':'Save'}
    testPage(student, '/englishessay/submitAssignment',"","Submitting assignment failed", urlencode(s1ass))

# teacher sees the submitted essays
testPage(admin, '/englishessay/adminessayresults?assignmentid=1&complete=0', '<td>Student 1 essay', 'Student essay missing')

# teacher set marking mode
testPage(admin,'/englishessay/adminopassignment?assignmentid=1&oper=marking', """<button class="btn" onclick="javascript:document.location='adminopassignment?assignmentid=1&oper=complete'">Complete</button>""","Set to marking failed")

#students mark
## work out how many iterations
repetitions = 3
N = NumberOfStudents
maxCombinations = math.factorial(N)/math.factorial(N-2)/math.factorial(2)
if maxCombinations< N*repetitions:
     repetitions = int(math.floor(maxCombinations / N))

for i,student in enumerate(studentArr):
    # s1 marks
    studentid = str(i+1)
    result = testPage(student,'/englishessay/', '''Student Marking: s%s''' % studentid,"EnglishEssay not ready for marking for s%s" % studentid)

    for r in range(repetitions):

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
        if r == repetitions-1:
            expectedText = "s%s - Done marking" % studentid
        else:
            expectedText =  "Student Marking: s%s" % studentid   
        result = testPage(student, '/englishessay/evalEssay',expectedText,"Submitting marking failed", urlencode(s1mark))

# teacher set marking mode
testPage(admin,'/englishessay/adminopassignment?assignmentid=1&oper=complete', """<button class="btn" onclick="document.location='adminessayresults?assignmentid=1&complete=1'">View</button> ""","Set to complete failed")

# Student view result before grading
for i,student in enumerate(studentArr):
    studentid = str(i+1)
    testPageRex(student,'/englishessay/', '''<td>None</td>([^<]*)<td>Student %s''' % studentid,"Student essay not correct after marking s%s" % studentid)
    testPage(student, '/englishessay/viewessay?essayid=%s' % studentid,"<b>Grade</b> : None<br/>","Submitting view essay mark failed")

## teacher grades
calcmarks = {"lowgrade":40, "highgrade":80, "assignmentid":1}
testPage(admin,'/englishessay/adminsubmitmarks', """<td>80.0</td>""","Set to complete failed", urlencode(calcmarks))







print "Tests done"
