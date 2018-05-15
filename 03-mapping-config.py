from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

engine = create_engine('oracle://system:secret@localhost:1521/xe', echo=True)

Base = declarative_base()


class UserDetails(Base):
    __tablename__ = 'py_users'

    user_id = Column(Integer, Sequence('py_user_id_gen', start=1000, increment=2), primary_key=True)
    fullname = Column(String(50), nullable=False, default='Guest')
    password = Column(String(50), nullable=False)
    email_id = Column(String(50), unique=True)

    def __repr__(self):
        return '<UserDetails full_name={}>'.format(self.fullname)


Base.metadata.create_all(engine)