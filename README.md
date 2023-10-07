HOSPITAL MANAGEMENT SYSTEM

This is a Python application for managing hospital records, including patients, doctors, and appointments. It uses the SQLAlchemy library to interact with a SQLite database, allowing you to perform various operations related to hospital management.

Setup
Clone the repository.

Install dependencies and enter the virtual environment:

pipenv install && pipenv shell
Initialize migrations

alembic init migrations
Edit alembic.ini file

sqlalchemy.url = your_db_connection_string

Edit env.py to import Base and set target_metadata

Create and upgrade models using:

alembic revision --autogenerate -m "message"
alembic upgrade head

Features
Create, read, update, and delete patient records.
Create, read, update, and delete doctor records.
Schedule and manage patient appointments with doctors.
View a list of available doctors and their specialties.
View a list of appointments for a specific doctor.
Cancel existing appointments.

