import sys
import math

for line in sys.stdin:
    r, x, y = list(map(float,line.split(' ')))

    #test if point in in the cookie
    if (math.sqrt(pow(x,2)+pow(y,2))>r):
        print("miss")
        continue

    #centers the point on the x-axis
    x = math.sqrt(pow(x,2)+pow(y,2))
    y = 0
    
    #finds the ycord on the circle
    xcirc = x
    ycirc = math.sqrt(r**2 - x**2)
    
    #finds the angle produced from 0 to that point
    ang = math.atan(ycirc/xcirc)

    #calculates the area of the arc circle, and subtracts the triangle area
    arcArea = r**2 * ang
    triArea = xcirc * ycirc
    totArea = math.pi * r**2

    #prints the areas of the two halves
    print(totArea - arcArea + triArea, arcArea-triArea)
