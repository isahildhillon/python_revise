class Animal:
    def __init__(self, name):
        self.name = name  

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

tommy = Dog("Tommy")


tommy.eat()
tommy.bark()
