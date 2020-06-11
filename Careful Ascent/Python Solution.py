x, y = list(map(int, input().split()))

#takes in inputs
shields = []
count = int(input())
for i in range (count):
    shields.append(list(map(float, input().split())))

if (count == 0):
    print (x/y)
else:
    #sorts into sequential order
    shields.sort(key = lambda a: a[0])
    eq = (shields[0][0])

    #calculates verticle speed by a1Vy1 + a2Vy2 ... = x
    #Solves for V basically
    for j in range (count):
        eq += shields[j][2] * (shields[j][1]-shields[j][0])
        if (j != count-1):
            eq += (shields[j+1][0] - shields[j][1])
    eq += (y - shields[count-1][1])
    print (x/eq)
