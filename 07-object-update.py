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

user = session.query(UserDetails).filter_by(user_id=1000).one()
print(user)
user.password = 'dust'
user.fullname='Steve'
user.email_id='steve_jobs@apple.com'
session.add(user)
session.commit()
