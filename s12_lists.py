demo_list = ["a", 1,  45, True, 6.777] # Initialize new list
print(len(demo_list)) # Get list length

range_list = list(range(10)) # Make list from range

# ----------------
# Accessing Values
# ----------------

friends = ["Ashley", "Matt", "Michael"]

print(friends[0]) # 'Ashley'
print(friends[-1]) # 'Michael'
print(friends[-3]) # 'Ashley'
#print(friends[-4]) # IndexError

# -----------------------------
# Check if a Value is in a List
# -----------------------------

is_ashley_in_list = "Ashley" in friends
print(is_ashley_in_list)
is_colt_in_list = "Colt" in friends
print(is_colt_in_list)

# ------------------------------
# Accessing All Values in a List
# ------------------------------

numbers = [1,2,3,4]

for number in numbers:
    print(number)

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# -------
# Methods
# -------

first_list = [1,2,3,4]
first_list.append(5) # Add an item to the end of the list --> [1, 2, 3, 4, 5]
first_list.extend([6,7,8,9]) # Add multiple items to the end of the list --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
first_list.insert(2, 'Hi') # Insert an item at the 2nd position --> [1, 2, 'Hi', 3, 4, 5, 6, 7, 8, 9]
first_list.insert(-1, 'The end!') # Insert an item at the end --> [1, 2, 'Hi', 3, 4, 5, 6, 7, 8, 'The end!', 9]

#... chapter 104