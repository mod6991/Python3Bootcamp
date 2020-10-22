# -----------------------
# Writing custom for loop
# -----------------------

def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            val = next(iterator)
        except StopIteration:
            break
        else:
            func(val)

def square(x):
    print(x*x)

my_for("lol", print)
my_for([1,2,3,4,5], square)

# ---------------
# Custom iterator
# ---------------

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

print()
for x in Counter(10,20):
    print(x)

# ---------
# Generator
# ---------

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

print()
counter = count_up_to(10)
for num in counter:
    print(num)

def fib_gen(max):
    x, y, count = 0, 1, 0
    while count < max:
        x, y = y, x+y
        yield x
        count += 1

print()
for num in fib_gen(15):
    print(num)
