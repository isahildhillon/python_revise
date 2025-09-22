class Person:
    def __init__(self,age):
        self._age = age

    @property
    def age(self):
        return self._age+2
    
    @age.setter
    def age(self,age):
        if 1<=age and age<=5:
            self._age=age
        else:
            raise ValueError("Age must be between 1 to 5")

daksh = Person(50)
print(daksh.age) # print age 52
# if we do
# daksh.age=10 
# error will come as not between 1 to 5

