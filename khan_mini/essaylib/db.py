from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import create_engine
from settings import *

metadata = MetaData()
engine = create_engine('sqlite:///%s' % ESSAY_DB, echo=True)
assignmentTable = Table('assignment', metadata, autoload = True, autoload_with= engine)
adminTable = Table('admin', metadata, autoload = True, autoload_with= engine)
essayTable = Table('essay', metadata, autoload = True, autoload_with= engine)
essayEvalTable = Table('essay_eval',metadata, autoload = True, autoload_with= engine)
commentTable = Table('comments', metadata, autoload = True, autoload_with= engine)

def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute('pragma foreign_keys=ON')

from sqlalchemy import event
event.listen(engine, 'connect', _fk_pragma_on_connect)




