# coding=utf-8
import os, sys
# append parent# -*- coding: ascii -*- directory to path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

import MySQLdb as mdb
from settings import *
from grade_items import *

#if(len(sys.argv) < 2):
#    print "Usage: python grade_items_XXX.py COURSEID"
#    sys.exit(0)
#courseid = sys.argv[1]   
courseid = 14

conn = mdb.connect(SERVER, USER, PASSWORD, MOODLE_DB);
c = conn.cursor()

deleteAllGradeItems(conn,c,courseid)

rootcatid,catid = makeCat(conn,c,courseid,"Reading Grade Level")
gradenames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[12]*len(gradenames), [0]*len(gradenames))

