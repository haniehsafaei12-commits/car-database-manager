from MODEL import car_attributes , Car
from sqlalchemy.exc import SQLAlchemyError

class Car_Controller():
        def add_cars(self ,Name , Model ,Color ,Horse_Power):
                try:
                        car_new=Car(Name=Name , Model=Model ,Color=Color ,Horse_Power=int(Horse_Power))
                        car_attributes.add(car_new)
                        car_attributes.commit()
                        return True
                except SQLAlchemyError as e:
                        print("ERROR!")
                        

        def delete_cars(self , key_):
                try:
                        machine= car_attributes.query(Car).filter(Car.Id == key_).first()
                        if machine:
                                car_attributes.delete(machine)
                                car_attributes.commit()
                                return True
                        else:
                                return False
                except SQLAlchemyError as e:
                        car_attributes.rollback()
                        return False
                  

        def update_cars(self , key_ ,Name , Model ,Color ,Horse_Power):
                try:
                        machine = car_attributes.query(Car).filter(Car.Id == key_).first()
                        if machine:
                                machine.Name = Name
                                machine.Model = Model
                                machine.Color = Color
                                machine.Horse_Power = Horse_Power
                                car_attributes.commit()
                                return True
                        else:
                                return False
                except SQLAlchemyError as e:
                        car_attributes.rollback()
                        return False

        def show_all_cars(self):
                try:
                        return car_attributes.query(Car).all()

                    
                except SQLAlchemyError as e:
                        return []

