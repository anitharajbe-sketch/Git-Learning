from sqlalchemy import create_engine, Column, String, Integer,ForeignKey, Date
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import IntegrityError
import random
from contextlib import contextmanager


engine = create_engine("sqlite:///anitha_favourites.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
	__tablename__ = 'users_name'
	id = Column(Integer, primary_key=True,unique=True)
	name = Column(String(200),nullable=False)
	phone = Column(Integer,nullable=False)
	date_of_birth = Column(Date,nullable=False)
	gender = Column(String(50),nullable=False)
	nationality = Column(String(50),nullable=False)

class Address(Base):
	__tablename__ = 'user_address'
	id = Column(Integer, ForeignKey('users_name.id'),primary_key=True,unique=True)
	address_line = Column(String(300),nullable=False)
	city = Column(String(200),nullable=False)
	state = Column(String(200),nullable=False)
	country = Column(String(200),nullable=False)
	zip_code = Column(Integer,nullable=False)

class UserEmail(Base):
	__tablename__ = 'users_email'
	id = Column(Integer,ForeignKey('users_name.id'),primary_key=True, unique=True)
	email = Column(String(200),nullable=False)
	password = Column(String(200),nullable=False)


Base.metadata.create_all(engine)

@contextmanager
def session_scope():
	session = Session()
	try:
		yield session
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()

def reg_users_with_address(name,phone,gender,date_of_birth,nationality,
                           address_line,city,state,country,zip_code,email,password):
	aadhar_no = random.randint(100000000000,999999999999)
	while True:
		user_obj = User(id=aadhar_no, name=name,
		                phone=phone,gender=gender, date_of_birth=date_of_birth,
		                nationality=nationality)
		try:
			with session_scope() as session:
				session.add(user_obj)
				insert_user_address(session, aadhar_no, address_line,city,state,country,zip_code)
				insert_user_email(session,aadhar_no,email,password)
			return aadhar_no
		except IntegrityError:
			continue


def insert_user_address(session,aadhar_no, address_line,city,state,country,zip_code):
	address_obj = Address(
		id=aadhar_no,
		address_line=address_line,
		city=city, state=state,
		country=country,
		zip_code=zip_code)
	session.add(address_obj)


def insert_user_email(session, aadhar_no,email,password):
	email_obj = UserEmail(id=aadhar_no, email=email, password=password)
	session.add(email_obj)
