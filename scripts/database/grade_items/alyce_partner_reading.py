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
courseid = 13

conn = mdb.connect(SERVER, USER, PASSWORD, MOODLE_DB);
c = conn.cursor()

deleteAllGradeItems(conn,c,courseid)

rootcatid,catid = makeCat(conn,c,courseid,"Fables with Clear Morals")
gradenames = ["Author’s Message", "Thin Clarifying Questions", "Author’s Message 2", "Thick Questions", "Theme", "Author’s Message 3", "Author’s Message Quiz (Question 1)", "Questioning Quiz (Question 2)", "Connections Quiz (Question 3)", "Author’s Message 2 Quiz (Question 4)", "Connections 2 Quiz (Question 5)", "Theme Quiz (Question 6)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Fables with Unclear Morals")
gradenames = ["Inferring Author’s Message", "Predictions", "Inferring Author’s Message 2", "Character Traits", "Types of Characters", "Theme", "Types of Characters Quiz (Question 1)", "Character Traits Quiz (Question 2)", "Visualizing Quiz (Question 3)", "Predictions Quiz (Question 4)", "Theme Quiz (Question 5)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Gcina Mhlophe")
gradenames = ["Identifying Setting", "Analyzing Setting", "Identify Plot Elements", "Identify Plot Elements 2", "Identify Plot Elements 3", "Identify Plot Elements 4", "Identify the Exposition", "Character Traits", "Analyze Setting 2", "Identify Plot Elements Quiz (Question 1)", "Evaluating Plot Elements Quiz (Question 2)", "Analyze Setting Quiz (Question 3)", "Character Traits/Compare and Contract Characters Quiz (Question 4)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Poetry")
gradenames = ["Author’s Point of View", "Metaphor", "Hyperbole", "Simile", "Personification", "Onomatopoeia", "Alliteration", "Rhyme Scheme", "Mood", "Personification Quiz (Question 1)",  "Hyperbole Quiz (Question 1)", "Simile Quiz (Question 1)", "Metaphor Quiz (Question 1)", "Onomatopoeia Quiz (Question 1)", "Alliteration Quiz (Question 1)", "Rhyme Scheme Quiz (Question 1)", "Rhythm Quiz (Question 1)", "Imagery Quiz (Question 2)", "Mood Quiz (Question 3)", "Symbolism (Question 4)", "Author’s Message (Question 4)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Biographies and Memoirs")
gradenames = ["Character’s Point of View", "Character’s Point of View 2", "Inferring Character’s Point of View", "Flashback", "Sequencing Quiz (Question 1)", "Flashback Quiz (Question 1)", "Summary, Narrator’s Point of View Quiz (Question 2)", "Summary, Minor Character’s Point of View Quiz (Question 3)", "Evaluate Author’s Craft Quiz (Question 4)", "Summary, Non-fiction Quiz (Question 5)", "Evaluate Author’s Craft, Non-fiction Quiz (Question 6)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Historical Fiction")
gradenames = ["Foreshadowing", "Dialogue", "Mood", "Mood Quiz (Question 1)", "Character Change Quiz (Question 2)", "Comic Relief Quiz (Question 3)", "Foreshadowing Quiz (Question 4)", "Symbolism Quiz (Question 5)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

