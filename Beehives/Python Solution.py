x = list(map(float, input().split()))

#runs until end
while (x[0]!=0.0 and x[1]!=0.0):
    rad, numb = x[0], int(x[1])
    points = []

    #takes in every point
    for i in range(numb):
        points.append(list(map(float, input().split())))
    
    #finds all points that are within the given distance
    sour = []
    for i in range(numb):
        for j in range(i+1, numb):
            dist = ((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)**(1/2) 
            l1, l2 = [points[i][0], points[i][1]], [points[j][0], points[j][1]]
            if (dist<=rad):
                if (l1 not in sour):
                    sour.append(l1)
                if (l2 not in sour):
                    sour.append(l2)

    #calculates length of sour and prints it
    lensour = len(sour)
    print ("{0} sour, {1} sweet".format(lensour, numb-lensour))
    x = list(map(float, input().split()))
