import datetime
import calendar

array = list(map(int,input().split(' ')))

print(calendar.day_name[datetime.date(2009,array[1],array[0]).weekday()])
