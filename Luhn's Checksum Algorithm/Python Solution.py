for i in range(int(input())):
    numbs = [int(x) for x in list(input())]

    for j in range(len(numbs)-2,-1,-2):
        y = numbs[j]*2
        if(y>9):
            numbs[j]=int(list(str(y))[0])+int(list(str(y))[1])
        else:
            numbs[j]=y
    print("PASS" if sum(numbs)%10==0 else "FAIL")
