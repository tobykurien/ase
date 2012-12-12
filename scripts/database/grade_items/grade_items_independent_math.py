import os, sys
# append parent directory to path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

import MySQLdb as mdb
from settings import *
from grade_items import *

if(len(sys.argv) < 2):
    print "Usage: python grade_items_XXX.py COURSEID"
    sys.exit(0)
courseid = sys.argv[1]   

conn = mdb.connect(SERVER, USER, PASSWORD, MOODLE_DB);
c = conn.cursor()

rootcatid,catid = makeCat(conn,c,courseid,"Logic")
gradenames = ["Simple Logic Tables", "Completing Two Way Tables", "Writing Clues for Logic Tables", "Introduction to Venn Diagrams", "Set Notation", "Logic and Venn Diagrams", "Logic and Venn Diagrams Advanced", "Fermi On Own", "Fermi On Own #2", "Write Own Fermi Problem with Proposed Answer"]
grademax = [4,5,3,8,6,7,5,1,1,3]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,grademax, [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Graphs")
gradenames = ["Reading Scatter Plots","Plotting Points","Plotting Negative Numbers","Plotting Polygons","Analyzing Line Graphs","Reading Conversion Graphs","Plotting Conversion Graphs"]
grademax = [4,4,4,7,4,3,2]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,grademax, [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Angles")
gradenames = ["Degrees & a Compass Rose","Measuring Angles","Angles on a Line & Around A Point","Constructing Triangles","Classifying Triangles","Finding Exterior Angles"]
grademax = [4,4,4,3,3,2]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,grademax, [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Perimeter and Area")
gradenames = ["Unit Conversion","Perimeter and Area of Squares & Rectangles","Conversion Between Perimeter and Area","Area and Perimeter of Squares and Rectangles Word Problems","Area of Compound Shapes by Using Formulas","Triangle Area by Using a Square","Triangle Area & Area of Compound Shapes with Triangles","Area of Negative Space","Area of Triangle Word Problems"]
grademax = [3,5,4,5,2,2,2,2,3]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,grademax, [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Data")
gradenames = ["Types of Data","Pictograms","Stem and Leaf Plots","Conversions & Proportions","Stacked Bar Charts","Pie Charts","Converting Between Data Displays"]
grademax = [3,2,4,11,2,2,1]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,grademax, [0]*len(gradenames))

