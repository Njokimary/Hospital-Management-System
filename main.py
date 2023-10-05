from sqlalchemy import Column, String, Integer, create_engine, ForeignKey, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime


db_url = "sqlite:///hospitals.db"
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
    appointments = relationship("Appointment", back_populates="patient")

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    specialty = Column(String)
    department = Column(String)
    phone = Column(Integer)
    email = Column(String)
    appointments = relationship("Appointment", back_populates="doctor")
class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    appointment_date = Column(Date)
    appointment_time = Column(DateTime)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")


# create a session
Session = sessionmaker(bind=engine)
session = Session()

# create all tables
Base.metadata.create_all(engine)

# create a patient instance
new_patient1 = Patient(first_name='John', last_name='Doe', gender='Male', contact=1234567890, email='johndoe@gmail.com')
session.add(new_patient1)
session.commit()

new_patient2 = Patient(first_name='Mary', last_name='Brown', gender='Female', contact=2233002345, email='marybrown@gmail.com')
session.add(new_patient2)
session.commit()


# create a doctor instance
new_doctor1 = Doctor(first_name='Jane', last_name='Smith', specialty='Cardiology', department='Cardiology', phone=1234567890, email='janesmith@example.com')
session.add(new_doctor1)
session.commit()

new_doctor2 = Doctor(first_name='James', last_name='Ice', specialty='Neurologist', department='Nerves', phone=222456900, email='jamesice@gmail.com')
session.add(new_doctor2)
session.commit()
