cases = [list(map(int, input().split())) for x in range(int(input()))]
caselen = len(cases)

#cycles through each case
for j in range(caselen):
    rang = range(cases[j][0], cases[j][1]+1)
    #cycles through each case again to check if they are matched
    for i in range(caselen):
        rang2 = range(cases[i][0], cases[i][1]+1)
        if (cases[i][0] in rang or cases[i][1] in rang):
            continue
        elif (cases[j][0] in rang2 or cases[j][1] in rang2):
            continue
        else:
            print ("edward is right")
            exit()
print ("gunilla has a point")
