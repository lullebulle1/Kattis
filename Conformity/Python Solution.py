mydict = {}

#takes in inputs and assigns to dictionary
for i in range(int(input())):
    x = list(input().split())
    x.sort()
    y = ' '.join(x)

    if (y in mydict.keys()):
        mydict[y] += 1
    else:
        mydict[y] = 1

#finds all possible numbers and finds max. Then finds amount with that
numbarr = [mydict[i] for i in mydict.keys()]
maxs = max(numbarr)
print (len([i for i in numbarr if i==maxs])*maxs)
