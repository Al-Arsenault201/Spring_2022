#In-class coding from Monday, May 9


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

a = MyClass
print(a)


class Car:
    def __init__(self):
        self.make = "Toyota"
        self.model = "Camry"
        self.vin = "12345678ABC789"
        self.license_plate = "PGV 369"


mycar = Car


#using a skeleton to define a class
class Car:
    def __init__(self,make,model, vin, license_plate):
        self.make = make
        self.model = model
        self.vin = vin
        self.license_plate = license_plate

mycar = Car("Toyota","Corolla","123454321","PGV 369")
my_car = Car('Toyota', 'Corolla', '12345', 'GoDogs')
your_car = Car("Tesla", "ModelY", "ABCDEFG","MyElectricCar")

d_Car = {
    "make":"",
    "model":"",
    "vin" : "",
    "license_plate": ""
}

my_d_Car = d_Car
my_d_Car["make"] = "Toyota"
my_d_Car["model"] = "Corolla"
my_d_Car["vin"] = "1233454321"
my_d_Car["license_plate"] = "PGV 369"

class Passenger:
    def __init__(self, name):
        self.name = name

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

class Car:
    def __init__(self,make,model, vin, license_plate):
        self.make = make
        self.model = model
        self.vin = vin
        self.license_plate = license_plate
        self.passengers = []

my_d_Car["Passengers"] = []
my_d_Car["Passengers"].append("ME")
