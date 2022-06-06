from datetime import date
from base_car_rent3 import Session, engine, Base
from cars import Car
from employees import Employee

# 1 - utworzenie bazy danych
Base.metadata.create_all(engine)

# 2 - utworzenie nowej sesji
session = Session()


# # 4 - utworzenie filmów
car1 = Car("ford focus",2000 )
ziomek1 = Employee("ziutek","ziolkowski","zielan", "maslo")
car2 = Car("subaru cośtam", 1998)

# # 5 - dodanie do sesji
session.add_all([car1, ziomek1,car2])


session.commit()
session.close()





