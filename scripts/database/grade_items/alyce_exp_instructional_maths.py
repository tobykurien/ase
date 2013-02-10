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
courseid = 9

conn = mdb.connect(SERVER, USER, PASSWORD, MOODLE_DB);
c = conn.cursor()

deleteAllGradeItems(conn,c,courseid)

rootcatid,catid = makeCat(conn,c,courseid,"Logic")
gradenames = ["1.1.Logic Puzzles", "1.2.Two Way Tables", "1.3.Sets and Venn Diagrams"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Graphs")
gradenames = ["3.1.Scatter Graphs", "3.2.Plotting Points", "3.3.Negative Numbers", "3.4.Coordinates", "3.5.Plotting Polygons", "3.6.Conversion Graphs"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Angles")
gradenames = ["5.1.Angles and Turns", "5.2.Measuring Angles", "5.3.Classifying Angles", "5.4.Angles on a Line and Angles on a Points", "5.5.Constructing Triangles", "5.6.Finding Angles in Triangles"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Area and Perimeter")
gradenames = ["9.1.Area", "9.2.Area and Perimeter", "9.3.The Area and Perimeter of a Rectangle", "9.4.Area of Compound Shapes", "9.5.Area of a Triangle"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Data")
gradenames = ["11.1.Types of Data", "11.2.Collecting Data"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Patterns")
gradenames = ["13.1.Pictorial Logic Patterns", "13.2.Extending Number Sequences", "13.3.Sequences with Geometric Shapes", "13.4.Two-Dimensional Number Patterns"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Quantitative Data")
gradenames = ["18.1.Data Presentation", "18.2.Measures of Central Tendency", "18.3.Measures of Dispersion", "18.4.Comparing Data", "18.5.Trends"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Scale Drawing")
gradenames = ["19.1.Measuring Lengths", "19.2.Plans", "19.3.Maps"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Volume")
gradenames = ["22.1.Concepts of Volume", "22.2.Volume of a Cube", "22.3.Volume of a Cuboid", "22.4.Capacity", "22.5.Density", "22.6.Volume of a Triangular Prism"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

