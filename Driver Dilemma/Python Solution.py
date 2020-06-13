#inputs
gallons, leak, distance = list(map(float, input().split()))
gallons /= 2
highest = 0 

#for every fuel economy input
for i in range (6):
    speed, mpg = list(map(float, input().split()))
    
    #calculates total gallons used by t*leak + t*v/mpg
    time = distance/speed
    gallonsused = time*leak + time*speed/mpg
    if (gallons - gallonsused > 0.000001):
        highest = speed
print ("YES {}".format(int(highest)) if highest!=0 else "NO")
