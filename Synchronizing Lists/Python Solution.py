x = int(input())

while(x!=0):
    #creates the arrays with blank elements
    initArr = [0]*x
    otherArr = [0]*x
    outArr = ['0']*x

    #takes in the first array
    for i in range(0,x):
        initArr[i]=int(input())

    #takes in the second array
    for j in range(0,x):
        otherArr[j]=int(input())

    #computes where the lowest number is and sticks the
    #lowest number from the second array at that index
    for k in range(0,x):
        indexMin = initArr.index(min(initArr))
        outArr[indexMin]=str(min(otherArr))
        initArr[indexMin] = 10001
        otherArr.remove(min(otherArr))

    #prints out the array
    print('\n'.join(outArr)+'\n')
    x = int(input())
