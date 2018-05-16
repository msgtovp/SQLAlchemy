from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker

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
Session = sessionmaker(bind=engine)
session = Session()

user = UserDetails(password='dust', fullname='Steve', email_id='steve_jobs@apple.com')
session.add(user)
session.commit()
session.add_all([
    UserDetails(password='test1', email_id='test1@domain.com'),
    UserDetails(password='test2', email_id='test2@domain.com'),
    UserDetails(password='test3', email_id='test3@domain.com'),
    UserDetails(password='test4', email_id='test4@domain.com')
])
session.commit()
