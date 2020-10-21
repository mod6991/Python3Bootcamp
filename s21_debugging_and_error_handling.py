# ----------------------
# Raising our own errors
# ----------------------

def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green")
    if type(color) is not str:
        raise TypeError("color must be instance of str")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid")
    print(f"Printed '{text}' in {color}")

colorize("blah blah", "blue")
#colorize("blah blah", "red") # ValueError: color is invalid
#colorize(3, "blue") # TypeError: text must be instance of str

# -------------------
# Handling exceptions
# -------------------

def play_numbers():
    while True:
        try:
            num = int(input("enter a number: "))
        except:
            print("That's not a number :(")
        else:
            print("The number is valid :)")
            break
        finally:
            print("RUNS NOT MATTER WHAT!")

def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("don't divide by zero please!")
    except TypeError:
        print("a and b mst be ints or floats")
    else:
        print(f"{a} divided by {b} is {result}")

def divide2(a,b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print("something went wrong")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")