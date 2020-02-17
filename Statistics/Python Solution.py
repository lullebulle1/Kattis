import sys

#for each line, calculates the min, max, and range
count = 1
for line in sys.stdin:
    x = list(map(int, line.split(' ')))
    x.pop(0)
    a, b = min(x), max(x)
    c = b-a

    print("Case {}: {} {} {}".format(count,a,b,c))
    count += 1
