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
courseid = 21

conn = mdb.connect(SERVER, USER, PASSWORD, MOODLE_DB);
c = conn.cursor()

deleteAllGradeItems(conn,c,courseid)

rootcatid,catid = makeCat(conn,c,courseid,"Within Word Pattern Early")
gradenames = ["Short/Long a", "Short/Long a", "Long a Patterns", "Short/Long e", "Short/Long e", "Short/Long e", "Short/Long I", "Short/Long I", "Short/Long o", "Long o Patterns", "Short/Long u", "Long u Patterns"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Within Word Pattern Middle")
gradenames = ["Less Common Long a", "R-influence a", "Less Common Long e", "R-influence e", "Long i Patterns", "R-blends/R-influenced I", "Ambiguous/Long o", "R-influenced o", "Other Long u", "R-influenced u", "R-blends/Vowels", "r-Influenced Vowels", "-ck, -k, -ke", "CVCe sorts across vowels", "CVVC across vowels"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Within Word Pattern Late")
gradenames = ["Diphthongs", "More Diphthongs", "Ambiguous Vowels", "Words Spelled with e", "Complex Consonants", "-tch and –ch", "-dge and –ge", "Hard and Sort c and g across vowels", "-ce, -ge, -ve, -se, -ze"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Syllables and Affixes Early")
gradenames = ["Sort for Sound of –ed", "Plural Words: -s and –es", "Plurals with –y", "Base Words + -ed and- ing", "Adding –ing: Double and e drop", "Adding –ed: Double and nothing", "Adding – ing: Double, e drop, nothing", "Past Tense Verbs"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Syllables and Affixes Middle")
gradenames = ["Compound Words", "More Compound Words", "Homophones", "More Homophones", "VCCV at Juncture (same/different)", "Syllable Juncture (VCCV, open VCV)", "VCV Open and Closed", "Closed VCCV/Open VCV", "Closed/Open with Endings", "VCC/CV, VC/CCV, and V/V", "-le and –el", "-er, -or, -ar", "Final –en, -on, -in, -ain", "Unaccented First Syllable", "/i/ sound", "Changing y to I", "Words by Parts of Speech"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Syllables and Affixes Late")
gradenames = ["Patterns for Long a", "Patterns for Long u and o", "Patterns for Long e and I", "Diphthongs in Multisyllable Words", "More Dipthongs", "Words with –ture, -sure, -cher", "Prefixes", "More Prefixes", "Number Prefixes", "Suffixes", "More Suffixes", "Special Consonants (hard/soft g)", "Special Consonants (hard/soft/final c)", "Special Consonants (que, ph, silent letters)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Derivational Relations Early")
gradenames = ["Adding –ion (-ct and -ss)", "e-Drop + -ion (-te, -ce, -se)", "sion and Spelling Changes", "e-Drop + -ation or –ition", "-ible and –able", "-able after e", "-ant, -ance, -ancy", "-ent, -ence, -ency", "-ary, -ery, -ory", "Prefixes Advanced", "Assimilated Prefixes", "More Assimilated Prefixes"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Derivational Relations Middle")
gradenames = ["Vowel Alteration in Related Pairs (long to short a, long a to schwa)", "Vowel Alteration in Related Pairs (long to short e, long e to schwa)", "Vowel Alteration in Related Pairs (long to short i, long i to schwa)", "Vowel Alteration in Related Pairs (long to short, long to schwa, schwa to short)", "Vowel Alteration in Related Pairs (schwa to short with -ity)", "Vowel Alteration in Related Pairs (long to short with –cation and -ation)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))

rootcatid,catid = makeCat(conn,c,courseid,"Derivational Relations Late")
gradenames = ["Latin Stems (jud, tract, spec)", "Latin Stems (vis, form, cred, por, dict)", "Latin Stems (duct, fer, press, spir)", "Latin Stems (aud, bene, cand/chand)", "Latin Stems (cap, cide, clud/clos/clus, cogn, corp)", "Latin Stems (dent/don’t, equa/equi, fac/fec, fid)", "Latin Stems (fin, flu, grac/grat, ject, junct)", "Latin Stems (langu/lingu, lit, mal, man)", "Latin Stems (mem, min, miss/mit, mob/mot)", "Latin Stems (pat, ped, pens/pend, pos/pon)", "Latin Stems (prim/princ, quir/ques, rupt, sal)", "Latin Stems (sci, scrib/script, sect/seg, sent/sens)", "Latin Stems (sequ/sec, son, stru)", "Latin Stems (tain/ten, tang/tact, tend/tens, term)", "Latin Stems (terra, tort/torq, vac, val)", "Latin Stems (ven/vent, vers/vert, voc, vol/volv)", "Greek Roots (aer, arch, aster/astr, auto)", "Greek Roots (bi/bio, centr, chron, cosm)", "Greek Roots (crat, crit, cycl, dem, derm)", "Greek Roots (geo, gram, graph, homo, hydra)", "Greek Roots (logo, logy, meter, micro)", "Greek Roots (ortho, pan, path, ped, phil)", "Greek Roots (phobia, phon, photo, phys)", "Greek Roots (pol, psych, scope, sphere)", "Greek Roots (tech, tele, therm, typ, zo)"]
makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[100]*len(gradenames), [0]*len(gradenames))


