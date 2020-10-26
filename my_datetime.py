from datetime import datetime, date, time, timedelta

dt = datetime.now()
print(dt.strftime("%d.%m.%Y %H:%M:%S.%f"))

d = date.today()
print(d.strftime("%d.%m.%Y"))

t = datetime.now().time()
print(t.strftime("%H:%M:%S.%f"))

# timedelta ctor params:
# weeks
# days
# hours
# minutes
# seconds
# milliseconds
# microseconds

dt2 = dt + timedelta(hours=-12, minutes=-50)
print(dt2.strftime("%d.%m.%Y %H:%M:%S.%f"))

dt3 = dt + timedelta(weeks=-1)
print(dt3.strftime("%d.%m.%Y %H:%M:%S.%f"))