from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:123@localhost/car_rent3", echo=True)

Session = sessionmaker(bind=engine)
Base = declarative_base()
