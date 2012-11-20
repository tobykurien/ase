from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import create_engine
from settings import *

metadata = MetaData()
engine = create_engine('sqlite:///%s' % ESSAY_DB, echo=True)
assignmentTable = Table('assignment', metadata, autoload = True, autoload_with= engine)
adminTable = Table('admin', metadata, autoload = True, autoload_with= engine)
essayTable = Table('essay', metadata, autoload = True, autoload_with= engine)
essayEvalTable = Table('essay_eval',metadata, autoload = True, autoload_with= engine)



