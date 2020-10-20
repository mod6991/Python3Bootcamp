# -----
# *args
# -----

def sum_all_nums(*args): # args is a tuple
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums(10,50,2,3,9))

numbers = [1,2,3,4,5,6]
print(sum_all_nums(*numbers)) # use '*' to pass a list of objects to a *args

# --------
# **kwargs
# --------

def print_kwargs_values(**kwargs): # kwargs is a dict
    for k,v in kwargs.items():
        print(f"{k}: {v}")

print_kwargs_values(test='blah', name='Jimi', age=27)

my_dict = { 'a': 1, 'b': 2, 'c': 3 }
print_kwargs_values(**my_dict) # use '**' to pass a dict to a **kwargs

# ------------------
# Parameter ordering
# ------------------

# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

def display_info(a, b, *args, instructor="Jimi", **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"*args count: {len(args)}")
    for arg in args:
        print(arg)
    print(f"instructor: {instructor}")
    print(f"**kwargs count: {len(kwargs)}")
    for k,v in kwargs.items():
        print(f"{k}: {v}")

print()
display_info(1,2,3,4,5, path='blah')