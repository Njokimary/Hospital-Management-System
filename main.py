from sqlalchemy import Column, String, Integer, create_engine, ForeignKey, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime


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
    first_name = Column(String)
    last_name = Column(String)
    specialty = Column(String)
    department = Column(String)
    phone = Column(Integer)
    email = Column(String)

class Appointment(Base):
    __tablename__ = 'appointments'
    appointment_date = Column(Date)
    appointment_time = Column(DateTime)