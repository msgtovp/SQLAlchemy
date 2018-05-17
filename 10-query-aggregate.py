from sqlalchemy import create_engine, func
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
        return '<UserDetails user_id={}, fullname={}, password={}, email_id={}>'.format(self.user_id, self.fullname, self.password, self.email_id)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
'''
session.add_all([
    UserDetails(password='test', email_id='van@python.org', fullname='Guido'),
    UserDetails(password='admin', email_id='james1@java.com', fullname='James'),
    UserDetails(password='test', email_id='rossum@python.org', fullname='Guido'),
    UserDetails(password='just', email_id='frank1@java.com', fullname='EdFrank'),
    UserDetails(password='good', email_id='chrish1@java.com', fullname='Chrish')
])
session.commit()
'''
nof_users = session.query(UserDetails).count()
print(nof_users)

users = session.query(func.count(UserDetails.fullname), UserDetails.fullname).group_by(UserDetails.fullname).all()
print(users)

users = session.query(func.sum(UserDetails.user_id), UserDetails.fullname).group_by(UserDetails.fullname).all()
print(users)
