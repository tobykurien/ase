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
courseid = 5

conn = mdb.connect(SERVER, USER, PASSWORD, MOODLE_DB);
c = conn.cursor()

deleteAllGradeItems(conn,c,courseid)

rootcatid,catid = makeCat(conn,c,courseid,"Arithmetic & Place Value")
gradenames = ["Place Value: Making Big and Small Whole Numbers", "Number Line Construction", "Number Systems", "Rounding Distorts Statistics", "Estimation in Real Life", "Estimate v. Actual", "Decimal Place Value", "Decimal Number Line", "Decimal Estimation"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Addition & Subtraction")
gradenames = ["Simple Addition & Subtraction with Brackets", "Double Digit Addition & Subtraction – Making It Easier", "Large Number Vertical Addition", "Large Number Vertical Subtraction", "Large Number Vertical Subtraction with Zeros", "Fixing Addition & Subtraction Mistakes", "Addition & Subtraction 1-Step Word Problems", "Addition & Subtraction 2-Step Word Problems", "Adding & Subtracting Decimals, Simple", "Fixing Adding & Subtracting Decimal Mistakes", "Adding & Subtracting Decimal Money Word Problems", "Adding & Subtracting Different Units as Decimals", "Adding & Subtracting 2-Step Decimals Word Problems", "Letter Substitutions"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Multiplication")
gradenames = ["Multiply & Divide Whole Numbers by Powers of 10", "Multiply & Divide Decimals by Powers of 10", "Secret Sums", "Secret Sums 2", "Secret Sums 3", "Secret Sums 4", "Fraction Method Decimal Multiplication", "Decimal Multiplication", "Multiplication 1-Step Word Problems", "Multiplication 2-Step Word Problems", "Egyptian Multiplication"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Division")
gradenames = ["BODMAS with Division", "Long Division Using Partial Quotient Method", "Secret Sums", "Divisibility Rules", "ISBN Numbers", "Dividing Decimals by Whole Numbers", "Division 1-Step Word Problems", "Division 2-Step Word Problems"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Number Patterns and Sequences")
gradenames = ["Gauss’ Trick", "Prime Factorization to Find Greatest Common Divisor", "Least Common Multiple Trick", "Finding Next Term in a Sequence", "Fibonacci’s Sequence", "Finding Next Term in a Geometric Sequence", "Generating Number Sequences, Single", "Generating Number Sequences, Double", "Generating Number Sequence Formulas", "Generating Number Sequence Formulas, Method 2", "Patterns with Lines", "Patterns with Regular Polygons", "Patterns with Word Problems", "Towers Pattern"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Fractions: An Introduction")
gradenames = ["Introduction to Fractions", "Equivalent Fractions", "Equivalent Fractions, Simplest Form", "Comparing Fractions", "Ordering Fractions", "Fractions of Quantities", "Fractions of Quantities Word Problems", "Mixed Number & Improper Fractions", "Mixed Number & Improper Fractions Conversion", "Comparing Mixed & Improper Fractions", "Ordering Mixed & Improper Fractions", "Mixed & Improper Fractions Word Problems", "What To Do When 150 People Show Up For Dinner, Part 1", "What To Do When 150 People Show Up For Dinner, Part 2"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Operations Review")
gradenames = ["Addition, Subtraction, Multiplication & Division Review", "Secret Sums", "Puzzles 1 & 2", "Number Puzzle", "Darts Puzzle", "Postcards Puzzle"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Time")
gradenames = ["To Come", "To Come"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Negative Numbers")
gradenames = ["To Come", "To Come"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Linear Equations")
gradenames = ["To Come", "To Come"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Decimals, Fractions and Percentages")
gradenames = ["To Come", "To Come"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Operations with Fractions")
gradenames = ["To Come", "To Come"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Probability")
gradenames = ["To Come", "To Come"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

