# ------
# Tuples
# ------

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December')

locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office"
}

cat = { 'name': 'biscuit', 'age': 0.5, 'favorite_toy': 'my chapstick' }
cat_items = cat.items() # dictionary items() returns list of tuples
                        # --> dict_items([('name', 'biscuit'), ('age', 0.5), ('favorite_toy', 'my chapstick')])

x = (1,2,3,3,3)
nb_1 = x.count(1) # Returns the number of times a value appears in a tuple --> 1
nb_3 = x.count(3) # 3
io1 = x.index(1) # Returns the index at which a value is found in a tuple --> 0

# ----
# Sets
# ----

s = set({1,2,3,4,5,5,5}) # Sets cannot have duplicates --> {1, 2, 3, 4, 5}
s2 = {1,2,3,4,5,5,5} # Another set --> {1, 2, 3, 4, 5}

is_4_in_s = 4 in s # True
is_8_in_s = 8 in s # False

s.add(8) # --> {1, 2, 3, 4, 5, 8}
s.add(5) # --> {1, 2, 3, 4, 5, 8}

s.remove(2) # --> {1, 3, 4, 5, 8}

s1 = { 50, 60, 70, 80, 90 }
s2 = { 55, 60, 65, 70, 75 }

s_union = s1 | s2 # --> {65, 70, 75, 80, 50, 55, 90, 60}
s_intersect = s1 & s2 # --> {60, 70}

set_comp = { num**2 for num in range(10) } # --> {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

string = "hello"
set_comp2 = { char for char in string if char in 'aeiouy' } # --> {'o', 'e'}
