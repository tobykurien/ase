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

weeks = ["14-Jan - 20-Jan","21-Jan - 27-Jan","15-Jan - 21-Jan","22-Jan - 28-Jan","16-Jan - 22-Jan","23-Jan - 29-Jan","30-Jan - 5-Feb","6-Feb - 12-Feb","13-Feb - 19-Feb","20-Feb - 26-Feb","27-Feb - 4-Mar","5-Mar - 11-Mar","12-Mar - 18-Mar","19-Mar - 25-Mar","26-Mar - 1-Apr","2-Apr - 8-Apr","9-Apr - 15-Apr","16-Apr - 22-Apr","23-Apr - 29-Apr","30-Apr - 6-May","7-May - 13-May","14-May - 20-May","21-May - 27-May","28-May - 3-Jun","4-Jun - 10-Jun","11-Jun - 17-Jun","18-Jun - 24-Jun","25-Jun - 1-Jul","2-Jul - 8-Jul","9-Jul - 15-Jul","16-Jul - 22-Jul","23-Jul - 29-Jul","30-Jul - 5-Aug","6-Aug - 12-Aug","13-Aug - 19-Aug","20-Aug - 26-Aug","27-Aug - 2-Sep","3-Sep - 9-Sep","10-Sep - 16-Sep","17-Sep - 23-Sep","24-Sep - 30-Sep","1-Oct - 7-Oct","8-Oct - 14-Oct","15-Oct - 21-Oct","22-Oct - 28-Oct","29-Oct - 4-Nov","5-Nov - 11-Nov","12-Nov - 18-Nov","19-Nov - 25-Nov","26-Nov - 2-Dec","3-Dec - 9-Dec","10-Dec - 16-Dec"]
for week in weeks:
	rootcatid,catid = makeCat(conn,c,courseid,week)
	gradenames = ["3","4","5","6","7","8","9"]
	makeGradeItem(conn,c,courseid,rootcatid,catid,gradenames,[10000]*len(gradenames), [0]*len(gradenames))

