import os
from datetime import datetime, date, time, timedelta

def GetFilesOlderThan(path, nb_days, now=datetime.now()):
    lst = []
    dir_content = os.scandir(path)
    for item in dir_content:
        if item.is_dir():
            lst.extend(GetFilesOlderThan(item.path, nb_days))
        elif item.is_file():
            stat = item.stat()
            modified = datetime.fromtimestamp(stat.st_mtime)
            modified_with_delta = modified + timedelta(days=nb_days)
            if now > modified_with_delta:
                lst.append({ 'modified': modified.strftime('%d.%m.%Y %H:%M:%S'), 'path': item.path })
    return lst

path_to_scan = [r'C:\Dev\Python']

full_lst = []

for path in path_to_scan:
    full_lst.extend(GetFilesOlderThan(path, 6))

nb_files = len(full_lst)
for item in full_lst:
    print(item)

print()
print(nb_files)