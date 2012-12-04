import MySQLdb as mdb
import time

MOODLE_DB = 'moodle'
USER = 'moodleuser'
PASSWORD='moodlepass'
SERVER = '192.168.1.10'
PREFIX = 'mdl_'

conn = mdb.connect(SERVER, USER, PASSWORD, MOODLE_DB);
c = conn.cursor()

rst = c.execute("select id, fullname from %scourse;" % PREFIX)  
rows = c.fetchall()

for row in rows:
    print "Busy with %s,%s" % row
    c.execute("""select id,courseid,parent,depth,path,fullname,aggregation,keephigh,droplow,
                         aggregateonlygraded,aggregateoutcomes,aggregatesubcats,
                         timecreated,timemodified,hidden from %sgrade_categories where courseid = %s and parent is null;""" % (PREFIX, row[0]))  
    rootcat = c.fetchall()
    if(len(rootcat) != 1):
        print "Something went wrong - more than one parent for %s,%s" % row
        continue
    for month in ('January','February','March'):    
        c.execute("select id from %sgrade_categories where courseid = %s and parent=%s and fullname='%s'  ;" % (PREFIX, row[0], rootcat[0][0], month))  
        rst = c.fetchall()
        if(len(rst)==0):
            rtcat =[r for r in rootcat[0]]
            rtcat[2] = rtcat[0]                     # set the parent to the root category
            rtcat[3] = 2                            # depth
            rtcat[5] = month                        # fullname
            rtcat[12] = int(time.time())            # timecreate
            rtcat[13] = int(time.time())            # timemodified
            del(rtcat[0])                           # don't want id
            c.execute("insert into "+PREFIX+"""grade_categories
                         (courseid,parent,depth,path,fullname,aggregation,keephigh,droplow,
                         aggregateonlygraded,aggregateoutcomes,aggregatesubcats,
                         timecreated,timemodified,hidden) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",rtcat )
        
            c.execute('SELECT LAST_INSERT_ID();')
            lastid = c.fetchone()[0]
            c.execute("""update %sgrade_categories set path='%s' where id = %s""" % (PREFIX, rtcat[3] + str(lastid)+"/", lastid))
            conn.commit()
            monthid = lastid
        else:
            monthid = rst[0][0]     
        for day in range(1,32):
            c.execute("select id from %sgrade_items where courseid = %s and parent=%s and fullname='%s'  ;" % (PREFIX, row[0], rootcat[0][0], month))           

