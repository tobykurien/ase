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
courseid = 20

conn = mdb.connect(SERVER, USER, PASSWORD, MOODLE_DB);
c = conn.cursor()

deleteAllGradeItems(conn,c,courseid)

rootcatid,catid = makeCat(conn,c,courseid,"Addition & Subtraction")
gradenames = ["Place Value (CIMT)", "Single Digit Addition", "Single Digit Subtraction", "Double Digit Plus Single Digit Addition (Including Decimals)", "Double Digit Minus Single Digit Subtraction (Including Decimals)", "Double Digit Addition (Including Decimals)", "Double Digit Subtraction (Including Decimals)", "Addition & Subtraction Word Problems (Including Decimals)", "Addition & Subtraction (CIMT)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Multiplication")
gradenames = ["Single Digit Multiplication", "Single & Double Digit by 10’s Unit Multiplication (Including Decimals)", "Single Digit Decimal Multiplication (Including Whole Number by Decimal)", "Double Digit by Single Digit Multiplication (Including Decimals)", "Multiplication Word Problems (Including Decimals)", "Multiplication (CIMT)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Division")
gradenames = ["Division Facts", "10’s Unit by 10’s Unit Division (Including Decimals)", "Double Digit by Single Digit Division", "Single Digit Decimal Division (Including Whole Number by Decimal)", "Double Digit by Single Digit Decimal Division", "Division Word Problems (Including Decimals)", "Division (CIMT)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Number Sense")
gradenames = ["Operations Review (CIMT)", "Logic (CIMT)", "Number Patterns & Multiples (CIMT)", "Angles (CIMT)", "Area & Perimeter & Unit Conversions (CIMT)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Fractions")
gradenames = ["Fraction of a Whole", "Simplifying Fractions", "Improper Fractions & Mixed Numbers", "Comparing Fractions", "Fractions (CIMT)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Data")
gradenames = ["Graphs (CIMT)", "Data (CIMT)", "Time (CIMT)", "Patterns (CIMT)", "Linear Equations (CIMT)", "Quantitative Data (CIMT)", "Decimals, Fractions & Percents (CIMT)", "Scale Drawing (CIMT)", "Operations with Fractions (CIMT)", "Probability (CIMT)", "Volume (CIMT)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Advanced Arithmetic")
gradenames = ["Triple Digit Addition (Including Decimals)", "Triple Digit Subtraction (Including Decimals)", "Addition & Subtraction Word Problems Advanced (Including Decimals)", "Double Digit Multiplication (Including Decimals)", "Triple Digit Multiplication (Including Decimals)", "Double Digit Division (Including Decimals)", "Multiplication & Division Word Problems Advanced (Including Decimals)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[1]*len(gradenames), [0]*len(gradenames))

