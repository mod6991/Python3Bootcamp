cat = { 'name': 'blue', 'age': 3.5, 'isCute': True }
cat2 = dict(name="kitty", age=0.5)

cat_age = cat["age"] # Accessing data in dictionary

# ------------------------------------
# Accessing all values in a dictionary
# ------------------------------------

for value in cat.values():
    print(value)

# ----------------------------------
# Accessing all keys in a dictionary
# ----------------------------------

print()
for key in cat.keys():
    print(key)

# ---------------------------------------------
# Accessing all keys and values in a dictionary
# ---------------------------------------------

print()
for key,value in cat.items():
    print(key,value)


# ------------------------------
# Check for keys in a dictionary
# ------------------------------

#cat["blahblah"] # KeyError
is_name_key_in_cat = "name" in cat # True
is_blah_key_in_cat = "blahblah" in cat # False

# --------------------------------
# Check for values in a dictionary
# --------------------------------

is_blue_value_in_cat = "blue" in cat.values() # True
is_name_value_in_cat = "name" in cat.values() # False

# -------
# Methods
# -------

#cat.clear() # Clears all the keys and values in a dictionary
cat2 = cat.copy() # Make a copy of a dictionary

new_user = {}.fromkeys(['name', 'age', 'email'], 'unknown') # --> {'name': 'unknown', 'age': 'unknown', 'email': 'unknown'}
username = new_user.get('name') # Retrieves a key in an object and return None if the key does not exist --> 'unknown'
no_key = new_user.get('blahblah') # idem --> None

email = new_user.pop('email') # Takes a key and removes that key-value pair from the dictionary. Returns the value
                              # unknown
                              # --> {'name': 'unknown', 'age': 'unknown'}

# popitem() removes a random key-value pair
second_dic = { 'gender': 'male', 'name': 'bob' }
second_dic.update(new_user) # Update keys and values in a dictionary and overwrites existing key-value pairs --> {'gender': 'male', 'name': 'unknown', 'age': 'unknown'}

comp_dic = { f"key{i}" : i**2 for i in range(1,4) } # --> {'key1': 1, 'key2': 4, 'key3': 9}
num_dic = { num : ("even" if num % 2 == 0 else "odd") for num in range(8) } # --> {0: 'even', 1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd'}
filtered_dic = { num : num**2 for num in range(8) if num % 2 == 0 } # --> {0: 0, 2: 4, 4: 16, 6: 36}
