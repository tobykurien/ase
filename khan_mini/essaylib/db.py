import sqlite3

def makeConnection(dbname):
    conn = sqlite3.connect(dbname)
    return conn

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


