import sqlite3
import datetime
import cherrypy

def makeConnection(dbname):
    conn = sqlite3.connect(dbname)
    return conn

def getNextId(conn, tablename):
    c = conn.cursor()
    c.execute('select max(id) from ' + tablename)
    result = c.fetchone()
    c.close()
    if result[0] == None:
        return 1
    else:
        return result[0]+1
    

def getPasswordHash(conn):
    c = conn.cursor()
    c.execute('select password from admin')
    result = c.fetchone()
    c.close()
    return result[0]

def listAssignments(conn, where='1=1', orderby='id desc'):
    c = conn.cursor()
    c.execute('select id, title, description, state, startdatetime from assignment where %s order by %s' % (where, orderby))
    result = c.fetchall()
    c.close()
    return result

def updateAssignment(conn, title, description,assignment_id=None):
    c = conn.cursor()
    startdatetime = (datetime.datetime.now().isoformat(' '))[:19]
    if assignment_id == None: # insert
        c.execute("insert into assignment (id, title, description, state, startdatetime) values (?,?,?,?,?)", (getNextId(conn, 'assignment'),title, description, 'READY', startdatetime))
    else:
        c.execute("UPDATE assignment set title=?, description=?, startdatetime=? where id=?",(title,description,startdatetime,assignment_id))
    conn.commit()
    c.close() 

def deleteAssignment(conn, assignment_id):
    c = conn.cursor()
    c.execute("delete from assignment where id=?",(assignment_id))
    conn.commit()
    c.close() 


def updateAssignmentState(conn, assignment_id, state):
    c = conn.cursor()
    startdatetime = (datetime.datetime.now().isoformat(' '))[:19]
    state = state.upper()
    c.execute("update assignment set startdatetime=?,state=? where id=?",(startdatetime,state,assignment_id))
    conn.commit()
    c.close() 


def listEssays(conn, cols="*", where='1=1', orderby='id'):
    c = conn.cursor()
    c.execute('select %s from essay where %s order by %s' % (cols,where, orderby))
    result = c.fetchall()
    c.close()
    return result
