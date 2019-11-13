from math import sqrt
x, y, x0, y0, x1, y1 = list(map(float,input().split(' ')))
dist = 0.0

if(y > y1):
    if(x < x0):
        dist = sqrt((x-x0)**2+(y-y1)**2)
    elif(x > x1):
        dist = sqrt((x-x1)**2+(y-y1)**2)
    else:        
        dist = y-y1
        
elif(y < y1 and y > y0):
    if(x < x0):
        dist = x0-x
    else:
        dist = x-x1
else:
    if(x < x0):
        dist = sqrt((x-x0)**2+(y-y0)**2)
    elif(x > x1):
        dist = sqrt((x-x1)**2+(y-y0)**2)
    else:        
        dist = y-y0

print(abs(dist))
