import math

for i in range(int(input())):
    x, y, angle = 0, 0, 90.0 
    for j in range(int(input())):
        pathang, pathdist = list(map(float, input().split()))
        angle += pathang
        x += pathdist * math.cos(angle*math.pi/180)
        y += pathdist * math.sin(angle*math.pi/180)

    print ("{0:0.6f} {1:0.6f}".format(x, y))
