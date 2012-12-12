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

rootcatid,catid = makeCat(conn,c,courseid,"Arithmetic & Place Value")
gradenames = ["Representing Numbers","Number Line 1","Place Value","Number Line 2","Number Line 3","Rounding Whole Numbers","Understanding Decimals Place Value","Rounding Numbers","Estimation with Decimals","Decimals on the Number Line 1","Decimals on the Number Line 2"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Addition & Subtraction")
gradenames = ["1-digit Addition","2-digit Addition","1-digit Subtraction","2- and 3-digit Subtraction","Addition with Carrying","4-digit Addition with Carrying","Subtraction with Borrowing","4-digit Subtraction with Borrowing","Addition and Subtraction Word Problems","Adding Decimals 0.5","Adding Decimals","Adding Decimals 2","Subtracting Decimals 0.5","Subtracting Decimals","Adding and Subtracting Decimals Word problems"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Multiplication")
gradenames = ["Basic Multiplication","Multiplying 1-digit Numbers","Multiplying 3-digits by 1-digit","Multiplication with Carrying","Multiplying 3-digits by 2-digits","Multi-digit Multiplication","Multiplication and Division Word Problems","Multiplying Decimals","Understanding Moving the Decimal"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Division")
gradenames = ["Basic Division","1-digit Division","Division without Remainders","Division with Remainders","Multi-digit Division","Multiplication and Division Word Problems","Dividing Decimals 1","Dividing Decimals 2","Dividing Decimals","Multiplication and Division Word Problems 2","Divisibility Intuition","Divisibility 0.5","Divisibility Tests","Divisibility"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Number Patterns & Sequences")
gradenames = ["Prime Numbers","Composite Numbers","Prime Factorization","The Fundamental Theorem of Arithmetic","Least Common Multiple","Greatest Common Divisor","Least Common Multiple and Greatest Common Divisor","Properties of Numbers 1","Properties of Numbers 2","Number Properties Terminology","Distributive Property","Order of Operations"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Fractions: An Introduction")
gradenames = ["Recognizing Fractions 0.5","Recognizing Fractions","Fractions on the Number Line",
"Equivalent Fractions","Equivalent Fractions 2","Simplifying Fractions","Comparing Fractions",
"Comparing Fractions 2","Order Fractions","Fractions Cut and Copy 1","Fractions Cut and Copy 2","Fractions on the Number Line 2","Fractions on the Number Line 3","Converting Mixed Numbers and Improper Fractions","Comparing Improper and Proper Fractions","Ordering Improper Fractions and Mixed Numbers"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Time")
gradenames = ["Telling Time 0.5","Telling Time","Telling Time 2"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Negative Numbers")
gradenames = ["Adding Negative Numbers","Adding and Subtracting Negative Numbers","Multiplying and Dividing Negative Numbers","Negative Number Word Problems"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Linear Equations")
gradenames = ["Evaluating Expressions in One Variable","Combining Like Terms","Combining Like Terms with Distribution","Writing Expressions","Evaluating Expressions in 2 Variables","One Step Equations","One Step Equations with Multiples"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Decimals, Fractions, & Percents")
gradenames = ["Converting Fractions to Decimals","Converting Decimals to Fractions 1","Converting Decimals to Fractions 2","Converting Decimals to Percents","Converting Percents to Decimals","Percentage Word Problems 1","Percentage Word Problems 2","Discount Tax and Tip Word Problems","Markup and Commission Word Problems"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Operations with Fractions")
gradenames = ["Adding Fractions with Common Denominators","Subtracting Fractions with Common Denominators","Fraction Word Problems 1","Adding Fractions","Subtracting Fractions","Adding and Subtracting Fractions","Simplifying Fractions","Multiplying Fractions 0.5","Multiplying Fractions","Dividing Fractions 0.5","Dividing Fractions","Multiplying Fraction Word Problems","Dividing Fractions Word Problems","Ordering Improper Fractions and Mixed Numbers","Adding and Subtracting Mixed Numbers 0.5","Adding and Subtracting Mixed Numbers 1","Multiplying Mixed Numbers 1"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Probability")
gradenames = ["Counting 1","Counting 2","Permutations","Probability 1","Combinations","Independent Probability","Expected Value","Permutations and Combinations","Dependent Probability","Probability with Permutations and Combinations"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

