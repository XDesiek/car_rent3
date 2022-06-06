from sqlalchemy import Column, String, Integer, Date

from base_car_rent3 import Base


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    year = Column(Integer)

    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f'{self.model}, {self.year} '
