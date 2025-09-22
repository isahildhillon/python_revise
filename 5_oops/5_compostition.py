class Engine:
    def __init__(self,engine_type):
        self.engine_type=engine_type
        print("Engine Started")

class Car:
    engine =Engine
    def __init__(self,name):
        self.name=name
        self.engine = self.engine("S54")

    def describe(self):
        print(f"{self.name} car has a {self.engine.engine_type} Engine")

my_car=Car("BMW E46 M3") 
# we dont called any methosd but when we initialized it it calls Engine init which prints "Engine Started"
# so engine started is printed


my_car.describe()
# output
# BMW E46 M3 car has a S54 Engine