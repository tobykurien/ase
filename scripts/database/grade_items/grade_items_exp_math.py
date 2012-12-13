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

rootcatid,catid = makeCat(conn,c,courseid,"Graphs")
gradenames = ["Ordering Negative Numbers","Graphing Points","Graphing Points and Naming Quadrants","Points on the Coordinate Plane","Quadrilateral Types"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Angles")
gradenames = ["Measuring Angles","Angle Types","Exploring Angle Parts","Complementary and Supplementary Angles","Vertical Angles","Vertical Angles 2","Angles Addition Postulate","Triangle Types","Angles 1","Triangle Angles 1","Angles 2","Congruent Angles","Parallel Lines 1","Alternate Interior Angles 2","Corresponding Angles 2","Alternate Exterior Angles 2","Same Side Interior Angles 2","Same Side Exterior Angles 2","Parallel Lines 2"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Area & Perimeter")
gradenames = ["Perimeter 1","Area 1","Perimeter of Squares and Rectangles","Area of Squares and Rectangles","Area of Triangles"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Data")
gradenames = ["Reading Tables 1","Reading Tables 2","Reading Stem and Leaf Plots","Reading Pictographs 1","Reading Pictographs 2"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Patterns")

rootcatid,catid = makeCat(conn,c,courseid,"Quantitative Data")
gradenames = ["Reading Bar Charts 1","Reading Bar Charts 2","Reading Bar Charts 3","Reading Line Charts 1","Creating Bar Charts 1","Plotting the Line of Best Fit","Exploring Mean and Median","Mean, Median, and Mode","Creating Box and Whisker Plots","Average Word Problems"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Scale Drawing")

rootcatid,catid = makeCat(conn,c,courseid,"Volume")
gradenames = ["Solid Geometry"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))


