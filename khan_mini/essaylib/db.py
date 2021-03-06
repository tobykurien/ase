from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import create_engine
from settings import *

metadata = MetaData()
engine = create_engine(ESSAY_DB, echo=True)
                #isolation_level="READ UNCOMMITTED", echo=True)
assignmentTable = Table('assignment', metadata, autoload = True, autoload_with= engine)
adminTable = Table('admin', metadata, autoload = True, autoload_with= engine)
essayTable = Table('essay', metadata, autoload = True, autoload_with= engine)
essayEvalTable = Table('essay_eval',metadata, autoload = True, autoload_with= engine)
commentTable = Table('comments', metadata, autoload = True, autoload_with= engine)





