from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


db_url = "sqlite:///hospital.db"
engine = create_engine(db_url)


Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    contact = Column(Integer)
    email = Column(String)

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    specialty = Column(String(100))
    department = Column(String(100))
    phone = Column(String(15))
    email = Column(String(100))