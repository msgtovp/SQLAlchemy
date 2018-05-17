from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper

engine = create_engine('oracle://system:secret@localhost:1521/xe', echo=True)

metadata = MetaData()

user = Table('py_employee', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(50)),
            Column('fullname', String(50)),
            Column('password', String(12))
        )


class Employee(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password


mapper(Employee, user)

metadata.create_all(engine)