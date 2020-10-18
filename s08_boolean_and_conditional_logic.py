# ------------------
# Getting user input
# ------------------

print("What's your favorite color?")
color_name = input()
if color_name:
    print(f"Your favorite color is {color_name} !")
else:
    print("You didn't say anything")

# ----------------------
# Conditional statements
# ----------------------

x = input("Enter a value for x: ")
x = int(x)
if x > 0 and x < 10:
    print("x is larger than 0 and smaller thant 10")
elif x >= 10:
    print("x is larger or equal to 10")
else:
    print("x is negative")
