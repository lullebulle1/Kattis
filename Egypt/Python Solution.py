x = list(map(int, input().split()))

while (x[0] != 0):
    if ((x[0]**2 + x[1]**2)**(1/2)):
        print ("right")
    else:
        print ("wrong")
    x = list(map(int, input().split()))
