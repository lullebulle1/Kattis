numb, dist = list(map(int, input().split()))
distcur = 0
time = 0

#for each light
for i in range(numb):
    d, r, g = list(map(int, input().split()))
    time += d - distcur
    
    #finds if the light is currently red
    if (time%(r+g) < r):
        time += r-time%(r+g)
    
    #adds distance
    distcur = d
print(time + dist-distcur)
