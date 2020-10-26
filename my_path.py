import os
from datetime import datetime, date, time

def print_names(sorted_obj):
    for obj in sorted_obj:
        print(obj.name)

lst = tuple(os.scandir("C:\\Users\\mod69\\Documents"))

print("directories :")
print("-------------")
sorted_obj = sorted(filter(lambda i: i.is_dir(), lst),
                    key=lambda i: i.name)
print_names(sorted_obj)

print()
print("files :")
print("-------")
sorted_obj = sorted(filter(lambda i: i.is_file(), lst),
                    key=lambda i: i.name)
print_names(sorted_obj)

print()
print("links :")
print("-------")
sorted_obj = sorted(filter(lambda i: i.is_symlink(), lst),
                    key=lambda i: i.name)
print_names(sorted_obj)
