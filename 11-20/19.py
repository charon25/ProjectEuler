import datetime as dt

date = dt.datetime(year=1901, month=1, day=1)

SUNDAY = 6

first_month_sunday = 0

while date.year <= 2000:
    if date.day == 1 and date.weekday() == SUNDAY:
        first_month_sunday += 1
    date += dt.timedelta(days=1)

print(first_month_sunday)