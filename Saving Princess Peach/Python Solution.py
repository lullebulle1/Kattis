obj, uniq = list(map(int, input().split()))
numbs = []

#takes in all the inputs into unique array
for i in range (uniq):
    x = int(input())
    if (x not in numbs):
        numbs.append(x)

#prints everything in the range
for j in range (obj):
    if (j not in numbs):
        print (j)

#prints the last line
print ("Mario got {0} of the dangerous obstacles.".format(len(numbs)))
