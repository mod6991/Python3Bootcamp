# ------
# Lambda
# ------

def square(num):
    return num * num
print(square(7))

square2 = lambda num: num * num
print(square2(8))

add = lambda a,b: a + b
print(add(8, 2))

# ---
# Map
# ---

nums = [2,4,6,8,10]
map_obj = map(lambda n: n**2 ,nums)
new_list = list(map_obj) # --> [4, 16, 36, 64, 100]

# ------
# Filter
# ------

nums = [1,2,3,4]
filter_obj = filter(lambda n: n % 2 == 0, nums)
new_list = list(filter_obj) # --> [2, 4]

# ------------------------
# Combining map and filter
# ------------------------

nums = [1,2,3,4,5,6,7,8,10]
map_obj = map(lambda n: n**2, filter(lambda n: n % 2 == 0, nums))
new_list = list(map_obj) # --> [4, 16, 36, 64, 100]

# ---------
# All & Any
# ---------

names = ['Charlie', 'Connor', 'Jimi']

all_res = all([name[0] == 'C' for name in names]) # False
any_res = any([name[0] == 'C' for name in names]) # True

# ------
# Sorted
# ------

nums = [4,6,1,30,55,23]
sorted_nums = sorted(nums) # --> [1, 4, 6, 23, 30, 55]
sorted_nums2 = sorted(nums, reverse=True) # --> [55, 30, 23, 6, 4, 1]

my_dict = [
    { 'name': 'Jimi', 'age': 27 },
    { 'name': 'Alfred', 'age': 70 },
    { 'name': 'Bruce', 'age': 45 }
]

sorted_name = sorted(my_dict, key=lambda item: item['name']) # --> [{'name': 'Alfred', 'age': 70}, {'name': 'Bruce', 'age': 45}, {'name': 'Jimi', 'age': 27}]
sorted_age = sorted(my_dict, key=lambda item: item['age']) # --> [{'name': 'Jimi', 'age': 27}, {'name': 'Bruce', 'age': 45}, {'name': 'Alfred', 'age': 70}]

# ---------
# Min & Max
# ---------

nums = [3,5,23,65]
min_num = min(nums) # 3
max_num = max(nums) # 65

names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

min_len = min(len(name) for name in names) # 3
min_name = min(names, key=lambda n: len(n)) # 'Tim'

# --------
# Reversed
# --------

reversed_range = list(reversed(range(10))) # --> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# ------------------
# Abs, Sum and Round
# ------------------

abs(-23) # 23
abs(3.444) # 3.444
abs(-3.444) # 3.444

sum([1,2,3]) # 6
sum([1,2,3], 10) # 16

round(12.2) # 12
round(12.7) # 13
round(2.84551, 2) # 2.85

# ---
# Zip
# ---

list1 = [43, 56, 11, 5]
list2 = [76, 44, 2, 0]

zip_res = list(zip(list1, list2)) # --> [(43, 76), (56, 44), (11, 2), (5, 0)]

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

zip_obj = zip(
    students,
    map(
        lambda pair: max(pair),
        zip(midterms, finals)
    )
)

list_res = list(zip_obj) # [('dan', 98), ('ang', 91), ('kate', 78)]

zip_obj = zip(
    students,
    map(
        lambda pair: max(pair),
        zip(midterms, finals)
    )
)

dict_res = dict(zip_obj) # {'dan': 98, 'ang': 91, 'kate': 78}