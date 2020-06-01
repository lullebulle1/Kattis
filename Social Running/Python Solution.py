#takes in the inputs
x = []
runners = int(input())
for i in range(runners):
    x.append(int(input()))

#first and 2nd to last is always alone
#cycles the array for all possible starts and finds lowest
lowcount = x[0]+x[-2]
for i in range(runners):
    x.append(x.pop(0))
    if (x[0]+x[-2] < lowcount):
        lowcount = x[0]+x[-2]

#prints the lowest
print (lowcount)
