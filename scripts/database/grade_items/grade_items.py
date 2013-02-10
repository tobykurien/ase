import time
from settings import PREFIX

def makeCat(conn,c,courseid,catname):
    c.execute("""select id,courseid,parent,depth,path,fullname,aggregation,keephigh,droplow,
                         aggregateonlygraded,aggregateoutcomes,aggregatesubcats,
                         timecreated,timemodified,hidden from %sgrade_categories where courseid = %s and parent is null;""" % (PREFIX, courseid))  
    rootcat = c.fetchall()
    if(len(rootcat) != 1):
        print "Something went wrong - more than one parent for %s,%s" % (courseid,catname)
        raise Exception("Stopped!")
    rootcatid = rootcat[0][0]
    c.execute("select id from %sgrade_categories where courseid = %s and parent=%s and fullname='%s'  ;" % (PREFIX, courseid, rootcatid, catname))  
    rst = c.fetchall()
    if(len(rst)==0):
        rtcat =[r for r in rootcat[0]]
        rtcat[2] = rtcat[0]                     # set the parent to the root category
        rtcat[3] = 2                            # depth
        rtcat[5] = catname                        # fullname
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
        catid = lastid
    else:
        catid = rst[0][0] 
        
    return rootcatid,catid

def makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,grademax, grademin):
    for i,itemname in enumerate(gradenames):
        c.execute("select id from %sgrade_items where courseid = %s and categoryid=%s and itemname='%s'  ;" % (PREFIX, courseid, catid, itemname))           
        rst = c.fetchall()
        if(len(rst)==0): # does not exist
            gradeitem = [courseid, catid, itemname, "manual", 1,grademax[i],grademin[i],int(time.time()), int(time.time()), i]                
            c.execute("insert into "+PREFIX+"""grade_items (
                   courseid,categoryid,itemname,itemtype,
                   gradetype,grademax,grademin,                       
                   timecreated,timemodified,sortorder) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """,gradeitem)
            conn.commit()
      
def deleteAllGradeItems(conn,c,courseid):
   c.execute("delete from %sgrade_categories where courseid = %s and parent is not null;" % (PREFIX, courseid))           
   c.execute("delete from %sgrade_items where courseid = %s;" % (PREFIX, courseid))           
   conn.commit()  

