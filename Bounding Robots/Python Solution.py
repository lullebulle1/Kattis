while True:
    #takes in inputs
    w, l = list(map(int, input().split()))
    if (w==0 and l==0):
        break

    #calculates distance and edges
    steps = int(input())
    xrob, xact, yrob, yact = 0, 0, 0, 0
    for i in range(steps):
        direct, amount = list(input().split())
        
        if (direct == "u"):
            yrob += int(amount)
            yact += int(amount)
        elif (direct == "d"):
            yrob -= int(amount)
            yact -= int(amount)
        elif (direct == "l"):
            xrob -= int(amount)
            xact -= int(amount)
        elif (direct == "r"):
            xrob += int(amount)
            xact += int(amount)

        if (xact < 0):
            xact = 0
        elif (xact > w-1):
            xact = w-1

        if (yact < 0):
            yact = 0
        elif (yact > l-1):
            yact = l-1
    print ("Robot thinks {0} {1}\nActually at {2} {3}\n".format(xrob, yrob, xact, yact))
