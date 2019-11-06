fullDict = {}
sortArr = []

for i in range(int(input())):
    cup = input().split(' ')
    try:
        int(cup[0][0])
    except:
        fullDict[cup[1]] = cup[0]
        sortArr.append(int(cup[1]))
    else:
        fullDict[str(int(cup[0])/2)] = cup[1]
        sortArr.append(int(cup[0])/2)

sortArr.sort()
for i in range(len(sortArr)):
    print(fullDict[str(sortArr[i])])
        
