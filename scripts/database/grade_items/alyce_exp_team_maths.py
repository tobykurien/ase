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
courseid = 8

conn = mdb.connect(SERVER, USER, PASSWORD, MOODLE_DB);
c = conn.cursor()

deleteAllGradeItems(conn,c,courseid)

rootcatid,catid = makeCat(conn,c,courseid,"Logic")
gradenames = ["Logic Tables", "Venn Diagrams", "Fermi Problems"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[12]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Graphs")
gradenames = ["Scatter Plots", "Line & Conversion Graphs"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[12]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Angles")
gradenames = ["Degrees & Direction and Angle Dissection", "Angles on a Line, Around a Point, in a Triangle, & Constructing Triangles & Angles in a Quadrilateral"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[12]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Area and Perimeter")
gradenames = ["Area", "Coffee Traveler, How Much Does it Cost to Paint the Classroom, & Triangle Area"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[12]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Data")
gradenames = ["Data"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[12]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Patterns")
gradenames = ["To Come","To Come"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[12]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Quantitative Data")
gradenames = ["To Come","To Come"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[12]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Scale Drawing")
gradenames = ["To Come","To Come"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[12]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Volume")
gradenames = ["To Come","To Come"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[12]*len(gradenames), [0]*len(gradenames))

