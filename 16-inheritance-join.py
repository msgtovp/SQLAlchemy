from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine('oracle://system:secret@localhost:1521/xe', echo=True)

Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'vehicle'
    vid = Column(Integer, primary_key=True)
    vname = Column(String(30))
    veh_type = Column(String(30))
    __mapper_args = {
        'polymorphic_identity': 'vehicle',
        'polymorphic_on': veh_type,
        'with_polymorphic': '*'
    }

class TwoWheeler(Vehicle):
    __tablename__ = 'two_wheeler'
    tid = Column(Integer, ForeignKey('vehicle.vid'), primary_key=True)
    tname = Column(String(30))
    __mapper_args = {
        'polymorphic_identity': '2-wheel'
    }


class FourWheeler(Vehicle):
    __tablename__ = 'four_wheeler'
    fid = Column(Integer, ForeignKey('vehicle.vid'), primary_key=True)
    fname = Column(String(30))
    __mapper_args = {
        'polymorphic_identity': '4-wheel'
    }


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

two = TwoWheeler(vid=101, vname='Pulsar', tid=101, tname='150CC')
session.add(two)
session.commit()

twos = session.query(TwoWheeler).all()
print(twos)