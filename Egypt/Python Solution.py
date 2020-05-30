x = list(map(float, input().split()))
x.sort()

while (x[0] != 0):
    if (x[0]**2 + x[1]**2 - x[2]**2 == 0):
        print ("right")
    else:
        print ("wrong")
    x = list(map(float, input().split()))
    x.sort()
