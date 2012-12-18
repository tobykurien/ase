import pycurl
import cStringIO
 
SERVER = "http://localhost:8081"


def makeCurlObject():
    c = pycurl.Curl()
    return c

def sendRequest(curlObject, path, postfields=None):
    buf = cStringIO.StringIO()
    c = curlObject
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.setopt(c.URL, SERVER+path)
    if postfields:
        c.setopt(c.POSTFIELDS, postfields)
    result = c.perform()
    result =  buf.getvalue()
    buf.close()
    return result


def testPage(curlObject, path, expectedText, message, postfields=None):
    result = sendRequest(curlObject, path, postfields)
    if result.find(expectedText )==-1:
       raise Exception(message)
    return True


    
c = makeCurlObject()     
testPage(c,'/login', "<title>Menu - KhanAcademy</title>","Login failed", 'username='+'s1')
testPage(c,'/englishessay/', "Here is a list of your previous assignments","EnglishEssay failed")

#c.setopt(c.URL, '/englishessay/')
#c.perform()
