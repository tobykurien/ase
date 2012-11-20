import cherrypy
from cherrypy import request
from settings import *
import essaylib.db as db
import hashlib
from essaylib.saplugin import SAEnginePlugin, SATool
from sqlalchemy import and_, or_
import datetime
import random, math
import essaylib.scoring as scoring
import numpy



# Jinja templating engine
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

class EnglishEssay(object):       
        
    @cherrypy.expose    
    def index(self, username=None, essayeval_id=None):
        if username == None:
            username = cherrypy.session.get('username', None)
            if username == None:
                raise cherrypy.HTTPRedirect("/login")
        conn = request.db
        sql = "select distinct state from assignment"
        state = [s['state'] for s in conn.execute(sql).fetchall()]
        if 'BUSY' in state:
            a = self.activeAssignment(conn, 'BUSY')
            esql = db.essayTable.select(and_(db.essayTable.c.student_name == username, db.essayTable.c.assignment_id == a['id']))
            e = conn.execute(esql).fetchall()
            essay_text = e[0]['essay_text'] if len(e)>0 else ''
            return env.get_template('studentbusy.html' ).render({'username':username, 'asm':a,'essay_text':essay_text }) 
        elif 'MARKING' in state:
            a = self.activeAssignment(conn, 'MARKING')
            esql = db.essayEvalTable.select(and_(db.essayEvalTable.c.student_name == username, db.essayEvalTable.c.assignment_id == a['id'])).order_by(db.essayEvalTable.c.id)
            e = conn.execute(esql).fetchall()
            ids = [i['id'] for i in e]
            if essayeval_id == None:
                i = 0
            else:
                evalid = int(essayeval_id)
                if evalid in ids:
                    i = ids.index(evalid)
                    i = 0 if i == len(ids)-1 else i+1
                else:
                    i = 0
            essay1_text = self.getEssayText(conn, e[i]['essay1_id'])
            essay2_text = self.getEssayText(conn, e[i]['essay2_id'])
            score2 = e[i]['score2']
            if score2 == None:
                 score2 = 0.5
            p = {'username':username, 'essay1_text':essay1_text, 'essay2_text':essay2_text, 'essayeval_id':ids[i],'asm':a,'score':score2}  
            return env.get_template('studentmarking.html').render(p) 
        elif state == 'COMPLETED':
            return env.get_template('studentcomplete.html').render({'username':username}) 
        else:
            return env.get_template('studentready.html').render({'username':username}) 

    def activeAssignment(self,conn, state):
        asql = db.assignmentTable.select(db.assignmentTable.c.state == state)
        a = conn.execute(asql).fetchone()
        return a
     
    def getEssayText(self,conn, essayid):
        esql = db.essayTable.select(db.essayTable.c.id == essayid)
        e = conn.execute(esql).fetchone()
        return e['essay_text']

    @cherrypy.expose
    def evalEssay(self, scorerange, essayeval_id, bsubmit):
        conn = request.db
        sql = db.essayEvalTable.update().where(db.essayEvalTable.c.id == essayeval_id).values({'score1': 1.0-float(scorerange), 'score2':float(scorerange)})
        conn.execute(sql)
        return self.index(essayeval_id = essayeval_id)



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
            esql = db.essayEvalTable.delete(db.essayEvalTable.c.assignment_id == assignmentid)
            e = conn.execute(esql)
            esql = db.essayTable.select(db.essayTable.c.assignment_id == assignmentid)
            e = conn.execute(esql)
            essays = conn.execute(esql).fetchall()
            repetitions = 3
            N =  len(essays)
            maxCombinations = math.factorial(N)/math.factorial(N-2)/math.factorial(2)
            if maxCombinations< N*repetitions:
                 repetitions = int(math.floor(maxCombinations / N))
            if repetitions >= 1:
                pairs = self.assignPairs(N, repetitions)
                for i in range(N):
                    for j in range(repetitions):
                        student_name = essays[i]['student_name']
                        index = i*repetitions+j
                        essay1 = essays[pairs[index][0]]['id']
                        essay2 = essays[pairs[index][1]]['id']
                        esql = db.essayEvalTable.insert().values({'assignment_id':assignmentid, 'student_name':student_name ,'essay1_id':essay1, 'essay2_id':essay2})
                        conn.execute(esql)
        
        if state == "COMPLETED":
            esql = "select id from essay where assignment_id = %s order by id" % (int(assignmentid)) #db.essayTable.select(db.essayTable.c.assignment_id == assignmentid)
            e = conn.execute(esql)
            essays = conn.execute(esql).fetchall()
            ids = [i['id'] for i in essays]

            esql = db.essayEvalTable.select(db.essayEvalTable.c.assignment_id == assignmentid)
            e = conn.execute(esql).fetchall()
            A = numpy.matrix(numpy.zeros((len(ids),len(ids))))
            for i in e:
                row = ids.index(i['essay1_id'])
                col = ids.index(i['essay2_id'])
                A[row,col] = i['score1']
                A[col,row] = i['score2']
            c = scoring.colley(A)
            c1 = scoring.standardize(c)
            for i,id in enumerate(ids):
                sql = db.essayTable.update().where(db.essayTable.c.id == id).values({'score': c1[i]})
                conn.execute(sql)   
                

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

    def assignPairs(self, essaysCount, numberToSelect):
        result = []
        essayIndex = 0

        while essayIndex < essaysCount:
            numberIndex = 0
            while numberIndex < numberToSelect:
                a = random.randint(0, essaysCount-1)
                b = random.randint(0, essaysCount-1)
                if (a,b) not in result and (b,a) not in result and not a==b and not a==essayIndex and not b==essayIndex:
                    result.append((a,b))
                    numberIndex += 1
            essayIndex += 1
        return result



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
