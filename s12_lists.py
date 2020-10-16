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
first_list.clear() # Remove all items from the list --> []

first_list = [1,2,3,4]
first_list.pop() # Remove & returns last item in the list (4)
first_list.pop(1) # Remove the item at the given position in the list, and return it (2)

first_list = [1,2,3,4,4,4]
first_list.remove(2) # Remove the first item from the list whose value is 2 --> [1, 3, 4, 4, 4]
first_list.remove(4) # idem --> [1, 3, 4, 4]

numbers = [5,6,7,8,9,10]
numbers.index(6) # Returns the index of the specified item in the list (1)
numbers.index(9) # Returns the index of the specified item in the list (4)
numbers = [5,5,6,7,5,8,8,9,10]
numbers.index(5) # 0
numbers.index(5,1) # 1
numbers.index(5,2) # 4
numbers.index(8,6,8) # 6

numbers = [1,2,3,4,3,2,1,4,10,2]
numbers.count(2) # Return the number of times 2 appears in the list (3)
numbers.count(21) # 0
numbers.count(3) # 2

numbers = [1,2,3,4]
numbers.reverse() # Reverse the elements of the list (in-place) --> [4, 3, 2, 1]

numbers = [6,4,1,2,5]
numbers.sort() # Sort the items of the list (in-place) --> [1, 2, 4, 5, 6]

words = ['Coding', 'Is', 'Fun!']
' '.join(words) # 'Coding Is Fun!

# -------
# Slicing
# -------

# the_list[start:end:step]

numbers = [1,2,3,4]
numbers[1:] # Slice from position 1 to end --> [2, 3, 4]
numbers[3:] # Slice from position 3 to end --> [4]
numbers[-1:] # Slice from position -1 to end --> [4]
numbers[-3:] # Slice from position -3 to end --> [2, 3, 4]

numbers[:2] # Slice from start to position 2 --> [1, 2]
numbers[:4] # Slice from start to position 4 --> [1, 2, 3, 4]
numbers[1:3] # Slice from position 1 to position 3 --> [2, 3]

numbers = [1,2,3,4,5,6]
numbers[1::2] # Slice from position 1 to end with steps of 2 --> [2, 4, 6]
# !!! with negative steps, reverse the order
numbers[:1:-1] # Slice from start to position 1 in reverse --> [6, 5, 4, 3]
numbers[2::-1] # Slice from position 2 to end in reverse --> [3, 2, 1]

# Trick1: reversing lists/strings
string = "This is fun!"
string[::-1] # --> '!nuf si sihT'

# Trick2: Modifying portions of lists
numbers = [1,2,3,4,5]
numbers[1:3] = ['a','b','c'] # --> [1, 'a', 'b', 'c', 4, 5]

# ---------------
# Swapping Values
# ---------------

names = ["James", "Michelle"]
names[0], names[1] = names[1], names[0] # swap values --> ['Michelle', 'James']