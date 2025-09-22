class Student:
    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name
    
roll1 = Student("Sahil")
print(roll1.getName())

print(type(roll1))