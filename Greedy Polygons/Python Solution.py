import math
#the area of a n-polygon: na^2/(4tan(180/n))
    
amount = int(input())
for i in range(amount):
    n, l, d, g = list(map(int, input().split()))
    areainit = n * l**2 / (4*math.tan(math.pi/n)) 

    #adds circle rings for every increment
    #also adds rectangles to calculate new distance
    for j in range(g):
        newarea = areainit + math.pi*((d*(j+1))**2 - (d*j)**2) + n*d*l 
        areainit = newarea

    print (areainit)
