class Person:
    def __init__(self,name):
        self.name=name

    @classmethod
    def change_species(self,species):
        self.species=species
    
    @classmethod
    def from_fullName(cls,full_name):
        first_name=full_name.split()[0]
        return cls(first_name) # returning a new instance of the class by calling the class (cls) with the argument first_name.
    
Person.change_species("Human")
person1 = Person.from_fullName("Sahil Dhillon")

print(person1.species)
print(person1.name)

