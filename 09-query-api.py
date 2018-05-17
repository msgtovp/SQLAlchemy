from sqlalchemy import create_engine, and_
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

users = session.query(UserDetails).filter(UserDetails.fullname=='Steve').all()
print(users)
users = session.query(UserDetails).filter(UserDetails.fullname!='Steve').all()
print(users)
users = session.query(UserDetails).filter(UserDetails.fullname.like('%e%')).all()
print(users)
users = session.query(UserDetails).filter(UserDetails.fullname.ilike('%S%')).all()
print(users)
users = session.query(UserDetails).filter(UserDetails.fullname.in_(['Guido', 'James', 'Patrick'])).all()
print(users)
users = session.query(UserDetails).filter(~UserDetails.fullname.in_(['Guido', 'James', 'Patrick'])).all()
print(users)
users = session.query(UserDetails).filter(and_(UserDetails.fullname.ilike('%S%'), UserDetails.password == 'dust')).all()
print(users)


users = session.query(UserDetails).filter(UserDetails.fullname.in_(
    session.query(UserDetails.fullname).filter(UserDetails.fullname.like("%e%"))
)).all()
print(users)