import datetime
from sys import stdin

#for each test case
for line in stdin:
    #takes in input, casts the times to dates
    month, day, year, t1, t2 = list(line.split())
    ft1 = datetime.datetime.strptime(t1, "%H:%M")
    ft2 = datetime.datetime.strptime(t2, "%H:%M")

    #calculates the difference in time and cast to integer array of H, M, S
    diff = list(map(int, str(ft2-ft1).split(":")))

    #prints everything formated
    print ("{0} {1} {2} {3} hours {4} minutes".format(month, day, year, diff[0], diff[1]))
