import os
from pathlib import PurePath, Path
from datetime import datetime, date, time

def print_info(sorted_obj, is_file):
    for obj in sorted_obj:
        if not is_file:
            print(obj.name)
        else:
            stat = obj.stat()
            created = datetime.fromtimestamp(stat.st_ctime).strftime("%d.%m.%Y %H:%M:%S")
            modified = datetime.fromtimestamp(stat.st_mtime).strftime("%d.%m.%Y %H:%M:%S")
            size = stat.st_size
            print(f"{obj.name:16} (created: {created}, modified: {modified}, size: {size})")


lst = tuple(os.scandir("C:\\Users\\mod69\\Documents"))

print("directories :")
print("-------------")
sorted_obj = sorted(filter(lambda i: i.is_dir(), lst),
                    key=lambda i: i.name)
print_info(sorted_obj, False)

print()
print("files :")
print("-------")
sorted_obj = sorted(filter(lambda i: i.is_file(), lst),
                    key=lambda i: i.stat().st_ctime)
print_info(sorted_obj, True)

print()
print("links :")
print("-------")
sorted_obj = sorted(filter(lambda i: i.is_symlink(), lst),
                    key=lambda i: i.name)
print_info(sorted_obj, True)
