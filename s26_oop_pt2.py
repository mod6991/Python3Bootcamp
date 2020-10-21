# --------------------
# Properties (get/set)
# --------------------

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age < 0:
            raise ValueError(f"Age cannot be negative")
        self._age = age

    def __repr__(self):
        return f"{self.first} {self.last} is {self.age}"

    @property # Getter
    def age(self):
        return self._age
    
    @age.setter # Setter
    def age(self, value):
        if value < 0:
            raise ValueError(f"Age cannot be negative")
        self._age = value

jimi = Human("Jimi", "Hendrix", 27)
print(jimi)
jimi.age = 12
print(jimi)

# -----
# Super
# -----

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def __repr__(self):
        return f"{self.name} is a {self.species}"
    
class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, "cat") # call __init__ of parent class without self
        self.breed = breed
        self.toy = toy

class Dog(Animal):
    pass

blue = Cat("Blue", "Scottish Fold", "String")
print(blue)
print(isinstance(blue, Animal))
print(isinstance(blue, Cat))
print(isinstance(blue, Dog))