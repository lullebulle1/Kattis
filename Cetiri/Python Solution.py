x = list(map(int, input().split()))
x.sort()

dif1 = x[1] - x[0]
dif2 = x[2] - x[1]

if (dif1 == dif2):
    print (x[2] + dif1)
elif (dif1 > dif2):
    print (x[0] + dif2)
elif (dif1 < dif2):
    print (x[1] + dif1)
