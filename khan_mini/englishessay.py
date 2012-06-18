import cherrypy
from settings import *
import essaylib.db
import hashlib


# Jinja templating engine
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

class EnglishEssay(object):               
    @cherrypy.expose    
    def index(self, username=None):
        if username == None:
            username = cherrypy.session.get('username', None)
            if username == None:
                raise cherrypy.HTTPRedirect("/login")                
        return "Hallo world" + username

    @cherrypy.expose    
    def admin(self, password=None, bsubmit=None):
        result = ''
        conn = essaylib.db.makeConnection(ESSAY_DB)
        if (not cherrypy.session.get('admin',False)):
            if (password == None):
                return env.get_template('adminlogin.html').render() 
            elif hashlib.sha224(password).hexdigest() == essaylib.db.getPasswordHash(conn):
                cherrypy.session['admin'] = True
            else:     
                return env.get_template('adminlogin.html').render() 

        rows = essaylib.db.listAssignments(conn)
        cols = ['Id','Title','Description','State','Date','Action']
        result = env.get_template('adminassignments.html').render({'rows':rows,'cols':cols})
        return result

    @cherrypy.expose    
    def adminessayresults(self, assignmentid):
        if cherrypy.session.get('admin',None) == None:
             return env.get_template('adminlogin.html').render()
        conn = essaylib.db.makeConnection(ESSAY_DB)
        rows = essaylib.db.listEssays(conn, where='assignment_id=%s' % int(assignmentid), cols = "student_name, submitteddatetime, score,substr(essay_text,1,50)||' .....', id ", orderby="score")
        assignmentTitle = essaylib.db.listAssignments(conn, where="id=%s" % int(assignmentid))[0][1]
        cols = ['Student','Submitted','Score','Essay','Action']
        result = env.get_template('adminessayresults.html').render({'rows':rows,'cols':cols,'assignmentTitle':assignmentTitle,'assignmentid':assignmentid})
        return result

    @cherrypy.expose    
    def adminviewessay(self, assignmentid, essayid):
        if cherrypy.session.get('admin',None) == None:
             return env.get_template('adminlogin.html').render()
        conn = essaylib.db.makeConnection(ESSAY_DB)
        row = essaylib.db.listEssays(conn, cols = "id,student_name, submitteddatetime, score,essay_text", where=" assignment_id=%s and id=%s " % (int(assignmentid),int(essayid)), orderby="score")[0]
        ids = essaylib.db.listEssays(conn, cols = "id", where=" assignment_id=%s " % (int(assignmentid)), orderby="score")
        ids = [i[0] for i in ids]
        i = ids.index(int(essayid))
        previousid =  ids[len(ids)-1] if i == 0 else ids[i-1]
        nextid =  nextid = ids[0] if i == len(ids)-1 else ids[i+1]
          
        assignmentTitle = essaylib.db.listAssignments(conn, where="id=%s" % int(assignmentid))[0][1]
        result = env.get_template('adminviewessay.html').render({'id':row[0],'student_name':row[1], 'submitteddatetime': row[2], 'score': row[3],'essay_text':row[4],'assignmentid':assignmentid,'assignmentTitle':assignmentTitle, 'previousid':previousid, 'nextid':nextid})
        return result
        
    @cherrypy.expose    
    def admineditassignment(self, oper, assignmentid=None, title=None, description=None, bsubmit=None):
        if cherrypy.session.get('admin',None) == None:
             return env.get_template('adminlogin.html').render()

        conn = essaylib.db.makeConnection(ESSAY_DB)
        if oper == 'edit':  
            essaylib.db.updateAssignment(conn, title, description,assignmentid)
        elif oper == 'add': 
            essaylib.db.updateAssignment(conn, title, description)
        elif oper == 'del': 
            essaylib.db.deleteAssignment(conn, assignmentid)                 
        
        if oper in ['edit','add','del']: 
             raise cherrypy.HTTPRedirect("admin")   
        else:
            if oper == "addnew":
                row = ["new","",""]
                oper = 'add'
            elif oper == "toedit":  
                row = essaylib.db.listAssignments(conn, where=' id=%s ' % int(assignmentid))[0]
                oper = 'edit'
            result = env.get_template('admineditassignments.html').render({'id':row[0],'title':row[1],'description':row[2],'oper':oper})
            return result


    def adminchangestate(self, state, assignmentid):
        conn = essaylib.db.makeConnection(ESSAY_DB)
        state = state.upper()
        busy = False
        if state == 'BUSY':  
            r = essaylib.db.listAssignments(conn, where="state='BUSY'")
            if(len(r) != 0):
                busy = True
        
        if not busy:        
            essaylib.db.updateAssignmentState(conn, assignmentid, state)

        raise cherrypy.HTTPRedirect("admin")   

    @cherrypy.expose    
    def adminstartassignment(self, assignmentid):
        if cherrypy.session.get('admin',None) == None:
             return env.get_template('adminlogin.html').render()
        return self.adminchangestate('BUSY',assignmentid)
        
    @cherrypy.expose    
    def adminreadyassignment(self, assignmentid):
        if cherrypy.session.get('admin',None) == None:
             return env.get_template('adminlogin.html').render()
        return self.adminchangestate('READY',assignmentid)

    @cherrypy.expose    
    def adminmarkassignment(self, assignmentid):
        if cherrypy.session.get('admin',None) == None:
             return env.get_template('adminlogin.html').render()
        return self.adminchangestate('MARKING',assignmentid)

    @cherrypy.expose    
    def admincompleteassignment(self, assignmentid):
        if cherrypy.session.get('admin',None) == None:
             return env.get_template('adminlogin.html').render()
        return self.adminchangestate('COMPLETED',assignmentid)


    

if __name__=="__main__":
    # load config for global and application
    cherrypy.config.update(khanconf)
    cherrypy.tree.mount(EnglishEssay(), '/englishessay', config=enlishessayconf)

    cherrypy.engine.start()
    cherrypy.engine.block()
