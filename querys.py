# 1 - imports
from base_car_rent3 import Session
from cars import Car
from employees import Employee


# 2 - utworzenie sesji
session = Session()

# 3 - pobranie wszystkich filmów
cars = session.query(Car).all()
employees = session.query(Employee).all()

# 4 - wypisanie informacji o filmie
print('\n### All employees:')
for employee in employees:
    print(f'{employee.name} {employee.surname}')
print('')

print('\n### All cars:')
for car in cars:
    print(f'model:{car.model}, year:{car.year}')
print('')

# 1 - filmy po  15-01-01
print('\n### one car  :')
car = session.query(Car) \
    .filter(Car.year <1999).one()
print(car,"\n")
# 5 - zamknięcie sesji
session.close()