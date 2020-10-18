x = 100 # Define a new variable
print(x) # Prints the variable x

var1, var2, var3 = 1, 99, 3 # Define multiple variables at once
print(var1, var2, var3) # Prints the variables

# Variables should be snake_case
# CAPITAL_SNAKE_CASE usually refers to constants (e.g. PI = 3.14)
# UpperCamelCase usually refers to a class

some_variable = None # null value is None

print(type(x)) # Method type() returns the type of a variable

# -------------
# Concatenation
# -------------

str1 = "hello"
str2 = "world"
concat_result = str1 + " " + str2 # Basic concatenation
print(concat_result)

# -----------------
# String formatting
# -----------------

x = 10

formatted_with_f_strings = f"I've told you {x} times already!" #F-Strings
print(formatted_with_f_strings)

formatted_with_format_method = "I've told you {} times already!".format(x) #.format method
print(formatted_with_format_method)

# -------
# Indexes
# -------

my_string = "yessir"

first_letter = my_string[0]
print(first_letter)

last_letter = my_string[-1]
print(last_letter)

# ---------------------
# Converting data types
# ---------------------

decimal = 12.9546486
integer = int(decimal)
print(integer)
string = str(decimal)
print(string)

