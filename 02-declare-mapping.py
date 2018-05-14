from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('mysql+mysqlconnector://root:@localhost/test', echo=True)

Base = declarative_base()


class UserDetails(Base):
    __tablename__ = 'py_users'

    user_id = Column(Integer, primary_key=True)
    full_name = Column(String(50))

    def __repr__(self):
        return '<UserDetails full_name={}>'.format(self.full_name)


Base.metadata.create_all(engine)



#SQLite Log
'''
2018-05-14 15:23:30,273 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2018-05-14 15:23:30,273 INFO sqlalchemy.engine.base.Engine ()
2018-05-14 15:23:30,275 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2018-05-14 15:23:30,277 INFO sqlalchemy.engine.base.Engine ()
2018-05-14 15:23:30,278 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("py_users")
2018-05-14 15:23:30,279 INFO sqlalchemy.engine.base.Engine ()
2018-05-14 15:23:30,285 INFO sqlalchemy.engine.base.Engine
CREATE TABLE py_users (
        user_id INTEGER NOT NULL,
        full_name VARCHAR,
        PRIMARY KEY (user_id)
)


2018-05-14 15:23:30,286 INFO sqlalchemy.engine.base.Engine ()
2018-05-14 15:23:30,286 INFO sqlalchemy.engine.base.Engine COMMIT
'''
#Oracle Log
'''
2018-05-14 15:38:58,591 INFO sqlalchemy.engine.base.Engine SELECT USER FROM DUAL
2018-05-14 15:38:58,591 INFO sqlalchemy.engine.base.Engine {}
2018-05-14 15:38:58,593 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60 CHAR)) AS anon_1 FROM DUAL
2018-05-14 15:38:58,593 INFO sqlalchemy.engine.base.Engine {}
2018-05-14 15:38:58,594 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS NVARCHAR2(60)) AS anon_1 FROM DUAL
2018-05-14 15:38:58,594 INFO sqlalchemy.engine.base.Engine {}
2018-05-14 15:38:58,595 INFO sqlalchemy.engine.base.Engine select value from nls_session_parameters where parameter = 'NLS_NUMERIC_CHARACTERS'
2018-05-14 15:38:58,595 INFO sqlalchemy.engine.base.Engine {}
2018-05-14 15:38:58,596 INFO sqlalchemy.engine.base.Engine SELECT table_name FROM all_tables WHERE table_name = :name AND owner = :schema_name
2018-05-14 15:38:58,597 INFO sqlalchemy.engine.base.Engine {'schema_name': 'SYSTEM', 'name': 'PY_USERS'}
2018-05-14 15:38:58,598 INFO sqlalchemy.engine.base.Engine
CREATE TABLE py_users (
        user_id INTEGER NOT NULL,
        full_name VARCHAR2(50 CHAR),
        PRIMARY KEY (user_id))


2018-05-14 15:38:58,599 INFO sqlalchemy.engine.base.Engine {}
2018-05-14 15:38:58,646 INFO sqlalchemy.engine.base.Engine COMMIT
'''