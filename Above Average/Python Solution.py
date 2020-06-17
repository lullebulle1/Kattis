from statistics import mean

#runs through each test case
for i in range(int(input())):
    x = list(map(int, input().split()))
    x.pop(0)
    avg = mean(x)
    #calculates the amount above average
    print ("{0:.3f}%".format(100*len([y for y in x if y>avg])/len(x), 3))
