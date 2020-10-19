from random import random

def flip_coin():
    r = random()
    if r > .5:
        print('heads')
    else:
        print('tails')

def divide(num1, num2): # with parameters
    return num1 / num2

def exponent(num1, num2=2): # With default value
    return num1**num2

def show_information(name="Jimi", is_dead=True):
    if name == "Jimi" and is_dead:
        print("You're dead Jimi")
    elif name == "Jimi":
        print("Aren't you dead Jimi ???")
    else:
        print(f"Hello {name}")

def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def math(num1, num2, fn=add):
    return fn(num1, num2)

flip_coin()
print(divide(10, 5))
print(exponent(4,3))
print(exponent(4))

show_information()
show_information("Jimi", True)
show_information("Jimi", False)
show_information(name="few")

print(math(10, 3))
print(math(10, 3, fn=substract))

print(exponent(num2=2, num1=10)) # Keyword argument