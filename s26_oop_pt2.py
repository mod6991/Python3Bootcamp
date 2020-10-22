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

# ------------
# Polymorphism
# ------------

class MyAnimal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")

class MyDog(MyAnimal):
    def speak(self):
        return "woof"

class MyCat(MyAnimal):
    def speak(self):
        return "meow"

d = MyDog()
print(d.speak())
c = MyCat()
print(c.speak())

# -----------------
# __magic__ methods
# -----------------
from copy import copy
class Character:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Character named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if not isinstance(other, Character):
            raise TypeError(f"Can't add {type(self)} and {type(other)}")
        return Character("newborn", self.last, 0)

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError(f"Can't multiply {type(self)} and {type(other)}")
        return [copy(self) for i in range(other)]

j = Character("Jimi", "Hendrix", 27)
print(j) # __repr__
print(len(j)) # __len__
k = Character("Joe", "Dalton", 46)
print(j + k) # __add__
print(j * 3) # __mul__