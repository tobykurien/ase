import cherrypy
from cherrypy import request
from settings import *
import essaylib.db as db
import hashlib
from essaylib.saplugin import SAEnginePlugin, SATool
from sqlalchemy import and_, or_
import datetime


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
        conn = request.db
        sql = db.assignmentTable.select([db.assignmentTable.c.state]).distinct()
        state = [s['state'] for s in conn.execute(sql).fetchall()]
        if 'BUSY' in state:
            asql = db.assignmentTable.select(db.assignmentTable.c.state == 'BUSY')
            a = conn.execute(asql).fetchall()
            esql = db.essayTable.select(and_(db.essayTable.student_name == username, db.essayTable.assignment_id == a['id']))
            e = conn.execute(esql).fetchall()
            essay_text = e[0]['essay_text'] if len(e)>0 else ''
            return env.get_template('studentbusy.html' ).render({'username':username, 'asm':a,'essay_text':essay_text }) 
        elif state == 'MARKING':
            return env.get_template('studentmarking.html').render({'username':username}) 
        elif state == 'COMPLETE':
            return env.get_template('studentcomplete.html').render({'username':username}) 
        else:
            return env.get_template('studentready.html').render({'username':username}) 

    @cherrypy.expose
    def submitAssignment(self, essay_text, assignmentid, bsubmit):
        username = cherrypy.session.get('username',None)
        if  username == None:
             raise cherrypy.HTTPRedirect("/login")
        conn = request.db

        sql = db.essayTable.delete().where(and_(db.essayTable.c.assignment_id == assignmentid,db.essayTable.c.student_name == username))
        conn.execute(sql)

        submitteddatetime = (datetime.datetime.now().isoformat(' '))[:19]
        sql = db.essayTable.insert().values({'student_name':username,'assignment_id':assignmentid,'essay_text':essay_text,'submitteddatetime':submitteddatetime})
        conn.execute(sql)
        return self.index() 


    @cherrypy.expose    
    def admin(self, password=None, bsubmit=None):
        result = ''
        conn = request.db
        if (not cherrypy.session.get('admin',False)):
            if (password == None):
                return env.get_template('adminlogin.html').render() 
            elif hashlib.sha224(password).hexdigest() == getPasswordHash(conn):
                cherrypy.session['admin'] = True
            else:     
                return env.get_template('adminlogin.html').render() 
        rowSql = db.assignmentTable.select().order_by(db.assignmentTable.c.id.desc())
        rows = conn.execute(rowSql).fetchall()
        result = env.get_template('adminassignments.html').render({'rows':rows})
        return result

    @cherrypy.expose    
    def adminessayresults(self, assignmentid):
        if cherrypy.session.get('admin',None) == None:
             return env.get_template('adminlogin.html').render()
        conn = request.db
        rowsSql = db.essayTable.select(db.essayTable.c.assignment_id == assignmentid)
        rows = conn.execute(rowsSql).fetchall()
        sql = db.assignmentTable.select(db.assignmentTable.c.id == assignmentid)
        assignmentTitle = conn.execute(sql).fetchone()['title']
        result = env.get_template('adminessayresults.html').render({'rows':rows,'assignmentTitle':assignmentTitle,'assignmentid':assignmentid})
        return result

    @cherrypy.expose    
    def adminviewessay(self, assignmentid, essayid):
        if cherrypy.session.get('admin',None) == None:
             return env.get_template('adminlogin.html').render()
        conn = request.db
        rowsSql = db.essayTable.select(and_(db.essayTable.c.assignment_id == assignmentid, db.essayTable.c.id == essayid))
        row = conn.execute(rowsSql).fetchone()

        # figure out the next and previous essay id
        idSql = db.essayTable.select(db.essayTable.c.assignment_id == assignmentid)
        ids = conn.execute(idSql).fetchall()
        ids = [i[0] for i in ids]
        i = ids.index(int(essayid))
        previousid =  ids[len(ids)-1] if i == 0 else ids[i-1]
        nextid =  nextid = ids[0] if i == len(ids)-1 else ids[i+1]

        sql = db.assignmentTable.select(db.assignmentTable.c.id == assignmentid)
        assignmentTitle = conn.execute(sql).fetchone()['title']
          
        result = env.get_template('adminviewessay.html').render({'row':row,'assignmentid':assignmentid,'assignmentTitle':assignmentTitle, 'previousid':previousid, 'nextid':nextid})
        return result
        
    @cherrypy.expose    
    def admineditassignment(self, oper, assignmentid=None, title=None, description=None, bsubmit=None):
        if cherrypy.session.get('admin',None) == None:
             return env.get_template('adminlogin.html').render()

        conn = request.db
        if oper == 'edit':  
            startdatetime = (datetime.datetime.now().isoformat(' '))[:19]
            sql = db.assignmentTable.update().where(db.assignmentTable.c.id == assignmentid).values({'title':title, 'description':description,'startdatetime':startdatetime})
            conn.execute(sql)
        elif oper == 'add': 
            startdatetime = (datetime.datetime.now().isoformat(' '))[:19]
            sql = db.assignmentTable.insert().values({'title':title, 'description':description,'state':'READY','startdatetime':startdatetime})
            conn.execute(sql)
        elif oper == 'del': 
            sql = db.assignmentTable.delete().where(db.assignmentTable.c.id == assignmentid)
            conn.execute(sql)
        
        if oper in ['edit','add','del']: 
             raise cherrypy.HTTPRedirect("admin")   
        else:
            if oper == "addnew":
                row = ["new","",""]
                oper = 'add'
            elif oper == "toedit":  
                sql = db.assignmentTable.select(db.assignmentTable.c.id == assignmentid)
                row = conn.execute(sql).fetchone()
                oper = 'edit'
            result = env.get_template('admineditassignments.html').render({'id':row[0],'title':row[1],'description':row[2],'oper':oper})
            return result


    def adminchangestate(self, state, assignmentid):
        conn = request.db
        state = state.upper()
        busy = False
        if state == 'BUSY':  
            sql = db.assignmentTable.select(or_(db.assignmentTable.c.state == 'BUSY',db.assignmentTable.c.state == 'MARKING'))
            r = conn.execute(sql).fetchall()
            if(len(r) != 0):
                busy = True
  
        if state == 'MARKING':
            pass
            #e = essaylib.db.listEssays(conn, cols='id', where="assignment_id=%s" % (int(assignmentid)) ) 
            #pairs =essaylib.pairs.assignPairs(e)
            #essaylib.db.insertEssayEval(conn, pairs, assignmentid)
        
        if not busy:        
            startdatetime = (datetime.datetime.now().isoformat(' '))[:19]
            sql = db.assignmentTable.update().where(db.assignmentTable.c.id == assignmentid).values({'state':state,'startdatetime':startdatetime})
            conn.execute(sql)


        raise cherrypy.HTTPRedirect("admin")   

    @cherrypy.expose    
    def adminopassignment(self, assignmentid,oper):
        if cherrypy.session.get('admin',None) == None:
             return env.get_template('adminlogin.html').render()
        if oper=='busy':
            return self.adminchangestate('BUSY',assignmentid)
        if oper=='ready':
            return self.adminchangestate('READY',assignmentid)
        if oper=='marking':
            return self.adminchangestate('MARKING',assignmentid)
        if oper=='complete':
            return self.adminchangestate('COMPLETED',assignmentid)

def getPasswordHash(conn):
    return conn.execute(db.adminTable.select()).fetchone()['password']
        

    

if __name__=="__main__":
    # load config for global and application
    cherrypy.config.update(khanconf)
    SAEnginePlugin(cherrypy.engine,ESSAY_DB).subscribe()
    cherrypy.tools.db = SATool()
    cherrypy.tree.mount(EnglishEssay(), '/englishessay', config=enlishessayconf)

    cherrypy.engine.start()
    cherrypy.engine.block()
