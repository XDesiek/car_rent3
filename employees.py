from sqlalchemy import Column, String, Integer, Date

from base_car_rent3 import Base


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    username = Column(String)
    password = Column(String)

    def __init__(self, name, surname,username,password):
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
