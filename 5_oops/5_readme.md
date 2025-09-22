# Class Object
 🔹 What is a Class?

A class is like a blueprint for creating objects. It defines properties (attributes) and methods (functions) that the objects created from the class will have.

🔹 What is an Object?

An object is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created.

# Atrribute Shadowing

```python

class MyClass:
    value = 10  # Class attribute

# Create an instance
obj = MyClass()

# Access class attribute
print(obj.value)  # Output: 10

# Shadow the class attribute by defining an instance attribute with the same name
obj.value = 20

# Now it uses the instance attribute
print(obj.value)  # Output: 20

# The class attribute is still 10
print(MyClass.value)  # Output: 10

del obj.value
print(obj.value) # print 10

```


> But if we do something like below

```python

class MyClass:
    value = 10  # Class attribute

# Create an instance
obj = MyClass()

# Access class attribute
print(obj.value)  # Output: 10

# Shadow the class attribute by defining an instance attribute with the same name
obj.value = 20

# Now it uses the instance attribute
print(obj.value)  # Output: 20

# The class attribute is still 10
print(MyClass.value)  # Output: 10

del obj.value
print(obj.value) # print 10

del obj.value # had no value of its own so delete what he got from class
print(obj.value) # Now an error will come as we dont have any value from class or object

```

--
🔎 What's Happening?


`obj.value = 20` does not change the class attribute.
Instead, it creates a new attribute value in the instance's __dict__, shadowing the one in the class.
--

# Self

```python

class Animal:
    weight = 100

    def animal_weight(self):
        return self.weight 

```

self works as a reference to all the variables like weight which are instance variable we can't return like `return weight` It has no reference to weight

A Class can't call the animal_weight it will give error because when an object pass calls a function in arguments it pass reference to the object


## 🔍 Let's Break It Down

### 🟩 1. Instance Method (like `animal_weight`)

* Defined with `def method(self):`
* Expects to be called **on an instance**, not on the class itself.
* `self` is **automatically passed** when you call the method through an object.

```python
elephant.animal_weight()  # Python passes `elephant` as `self`
```


---

### ❌ What if You Call It from the Class?

```python
print(Animal.animal_weight())
```

**This will throw an error:**

```python
TypeError: animal_weight() missing 1 required positional argument: 'self'
```

Because here you're calling the method on the **class**, and Python does **not automatically pass an instance**, so `self` is missing.

---

### ✅ How to Fix That?

If you still want to call it from the class, **you must manually pass an instance**:

```python
print(Animal.animal_weight(elephant))  # ✅ Output: 100
```

---


# Inheritance

```python
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

```


#  Composition

**Composition** is a design principle in **object-oriented programming (OOP)** where one class contains an **object of another class** as a **part of its state or behavior**. It’s often described as a "**has-a**" relationship.

---

### 🆚 Inheritance vs Composition

| Concept     | Relationship |
| ----------- | ------------ |
| Inheritance | "is-a"       |
| Composition | "has-a"      |

* Use **inheritance** when your class **is a type of** another class.
* Use **composition** when your class **uses or contains** another class.

---

### ✅ Simple Example: Composition

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car has an Engine

    def drive(self):
        self.engine.start()
        print("Car is moving")

# Create a car object
my_car = Car()

# Use methods
my_car.drive()
```

---

### 🖨️ Output:

```
Engine started
Car is moving
```

---

### 🔍 What’s Happening:

* The `Car` class **contains** an instance of `Engine`.
* When `my_car.drive()` is called:

  * It first calls `self.engine.start()` (delegation).
  * Then it prints that the car is moving.

---

### 📦 Real-World Analogy:

* A **Computer** has a **CPU**.
* A **Library** has many **Books**.
* A **Person** has a **Heart**.

---

### ✅ Another Example: Person and Address

```python
class Address:
    def __init__(self, city, country):
        self.city = city
        self.country = country

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # Composition

    def show_info(self):
        print(f"{self.name} lives in {self.address.city}, {self.address.country}")

# Create an Address object
addr = Address("New York", "USA")

# Pass it to a Person object
p1 = Person("Alice", addr)

p1.show_info()
```

---

### 🖨️ Output:

```
Alice lives in New York, USA
```

---

### 🔚 Summary:

* **Composition** lets you build complex types by combining objects.
* It's more flexible than inheritance and often better for **code reuse**.
* Helps in keeping **classes loosely coupled**.

---

>  we can achieve same thing using any of it but it is just illogical because we read it as "is a" or "has a"

# super
```python

class Animal:
    def __init__(self,name):
        self.name=name

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
```


# Method Resolution Order
```python
# Method resolution order
class A:
    def greet():
        print("Hello From Class A")


class B(A):
    def greet():
        print("Hello From Class B")

        
class C(A):
    def greet():
        print("Hello From Class C")

class D(B,C):
    pass

D.greet() # Hello From Class B

# if we add C first and B after that
class D(C,B):
    pass

D.greet() # Hello From Class C
# method or variable will be used from the first class which is inheritied

print(D.__mro__) 
```


# Static Methods
Which can be called directly by class we dont need any instance for it

```python

class School:
    @staticmethod
    def admission():
        print("We Are Open to Admissions")

School.admission()

```

# Class Methods

```python
class Person:
    def __init__(self,name):
        self.name=name

    @classmethod
    def change_species(cls,species):
        cls.species=species
    
    @classmethod
    def from_fullName(cls,full_name):
        first_name=full_name.split()[0]
        return cls(first_name) # returning a new instance of the class by calling the class (cls) with the argument first_name.
    
Person.change_species("Human")
person1 = Person.from_fullName("Sahil Dhillon")

print(person1.species)
print(person1.name)
```


# Class Method Vs Static Method


| Class Method | State Method |
|----|----|
|  Can Create Instance of Class| Can't Create instance of class  |
| Can Access\Update State of Class | Can't change access and state of class|
| First Argument is cls | Recevies Nothing (No Argument )|

> Class State refers to variables  data which are available across all the instances

# Dunders

Dunders are methods with double underscores before and after their names, like: __init__ , 

```python
str = "Hello sir"
print(str.__len__())
```

# Python Access Control Conventions

1. _name :- for protected
2. __name :- for private

> these can be access like self._name or _Person.__name But we should not do it . This is name mangling

# Getter , Setter

Get is used to get value of any property
Set is used to set its value

```python
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


```