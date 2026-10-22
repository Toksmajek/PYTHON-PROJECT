from pyclbr import Class


Raising errors in python

class Garage:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car(make={self.make}, model={self.model})>'

Class Garage:

    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"Tried to add a '{type(car).__name__}' to the garage. butyou can only add 'Car' objects.")
        self.cars.append(car)


ford = Garage()
car=Car("Ford", "Mustang")
ford.add_car(car)
print(len(ford))  # Output: 1