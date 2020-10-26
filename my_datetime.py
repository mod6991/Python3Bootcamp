from datetime import datetime, date, time

dt = datetime.now()
print(dt.strftime("%d.%m.%Y %H:%M:%S.%f"))

d = date.today()
print(d.strftime("%d.%m.%Y"))

t = time.now()
print(t.strftime("%H:%M:%S.%f"))
