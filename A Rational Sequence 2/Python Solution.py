def findSide(a,b,count):
    if(a==1 or b==1):
        return str(count)+","+str(a)+","+str(b)
    
    leftC = b-a
    rightC = a-b

    if(leftC<=0):
        return "r,"+findSide(rightC,b,count+1)
    elif(rightC<=0):
        return "l,"+findSide(a,leftC,count+1)
    else:
        return "failure"

for i in range(int(input())):
    prob, string = list(input().split(' '))
    a,b = list(map(int,string.split('/')))

    count = list(findSide(a,b,0).split(','))
    cordB = int(count.pop())
    cordA = int(count.pop())
    rowsDown = int(count.pop())

    line = max(cordA,cordB)

    if (cordA == 1):
        posX = 2**(rowsDown+line-1)-1

        rowsLeft = 0
        for j in count:
            rowsLeft*=2
            if(j=="r"):
                rowsLeft += 1
        print(prob, posX+rowsLeft+1)
    elif (cordB == 1):
        posX = 2**(rowsDown+line)-1
        rowsLeft = 0
        for j in count:
            rowsLeft*=2
            if(j=="l"):
                rowsLeft -= 1
        print(prob, posX+rowsLeft+1)
