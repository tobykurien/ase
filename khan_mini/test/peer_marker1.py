import pycurl
import cStringIO
from urllib import urlencode
 
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
    return True


student = makeCurlObject()     
testPage(student,'/login', "<title>Menu - KhanAcademy</title>","Login failed", 'username=s1')
testPage(student,'/englishessay/', "Here is a list of your previous assignments","EnglishEssay failed")

admin = makeCurlObject() 
testPage(admin,'/englishessay/admin', "<title>Assignments - KhanAcademy</title>","Admin login failed", 'password=x')
newass = {'assignmentid':'new','oper':'add','title':'My holiday','description':'My holiday'}
testPage(admin,'/englishessay/admineditassignment', "My holiday","New assignment failed", urlencode(newass))








#c.setopt(c.URL, '/englishessay/')
#c.perform()
