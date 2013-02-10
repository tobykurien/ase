import os, sys
# append parent directory to path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

import MySQLdb as mdb
from settings import *
from grade_items import *

#if(len(sys.argv) < 2):
#    print "Usage: python grade_items_XXX.py COURSEID"
#    sys.exit(0)
#courseid = sys.argv[1]   
courseid = 6

conn = mdb.connect(SERVER, USER, PASSWORD, MOODLE_DB);
c = conn.cursor()

deleteAllGradeItems(conn,c,courseid)

rootcatid,catid = makeCat(conn,c,courseid,"Arithmetic & Place Value")
gradenames = ["2.1.Place Value and Rounding", "2.2.Decimals and Place Values"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Addition & Subtraction")
gradenames = ["4.1.Addition and Subtraction", "4.2.Dealing with Money"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Multiplication")
gradenames = ["6.1.Multiplication of Whole Numbers","6.2.Long Multiplication", "6.3.Multiplying with Decimals","6.4.Multiplication Word Problems"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Division")
gradenames = ["8.1.Division of Whole Numbers","8.2.Long Division","8.3.Division Word Problems"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Number Patterns and Sequences")
gradenames = ["7.1.Multiples","7.2.Finding the Next Term","7.3.Growing Number Sequences","7.4.Formula for General Terms"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Fractions: An Introduction")
gradenames = ["10.1.Fractions","10.2.Equivalent Fractions","10.3.Fractions of Quantities","10.4.Mix Numbers and Improper Fractions"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Operations Review")
gradenames = ["12.1.Arithmetic with Whole Numbers and Decimals","12.2.Problems with Arithmetic"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Time")
gradenames = ["14.1.Telling Time","14.2.12 and 24 Hour Clocks", "14.3.Units of Time", "14.4.Timetables", "14.5.Time Problems in Context"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Negative Numbers")
gradenames = ["15.1.Addition and Subtraction of Negative Numbers" , "15.2.Multiplication and Division of Negative Numbers"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Linear Equations")
gradenames = ["16.1.Fundamental Algebraic Skills", "16.2.Function Machines" ,"16.3.Linear Equations"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Decimals, Fractions and Percentages")
gradenames = ["17.1.Conversion: Decimals into Fractions", "17.2.Conversion: Fractions into Decimals", "17.3.Introduction to Percentages", "17.4.Decimals, Fractions and Percentages"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Operations with Fractions")
gradenames = ["20.1.Whole Numbers and Decimals","20.2.Addition and Subtraction of Decimals", "20.3.Multiplying Fractions", "20.4.Dividing Fractions"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Probability")
gradenames = ["21.1.Introduction to Probability", "20.2.Calculating the Probability of a Single Event", "21.3.Relative Frequency", "21.4.Complementary Events", "21.5.Estimating Number of Outcomes", "21.6.Addition Law for Mutually Exclusive Events", "21.7.General Addition Law"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

