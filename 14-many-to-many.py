from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Table
from sqlalchemy.orm import relationship

engine = create_engine('oracle://system:secret@localhost:1521/xe', echo=True)

Base = declarative_base()

user_card_map = Table('py_user_cards', Base.metadata, 
    Column('owner', String(50), ForeignKey('py_user_details.username')),
    Column('card', Integer, ForeignKey('py_card_details.card_id'))
)

class UserDetails(Base):
    __tablename__ = 'py_user_details'
    username = Column(String(50), primary_key=True)
    fullname = Column(String(60))
    email_id = Column(String(60))
    password = Column(String(60), nullable=False)
    cards = relationship('UserCards', secondary=user_card_map)

class UserCards(Base):
    __tablename__ = 'py_card_details'
    card_id = Column(Integer, primary_key=True)
    card_number = Column(Integer, nullable=False)
    card_type = Column(String(40))
    user = relationship('UserDetails')

Base.metadata.create_all(engine)