#for each test case
for i in range(int(input())):
    #takes in that test cast
    x = list(map(int,input().split(' ')))
    
    #if the length is only 3, print 1
    if (len(x)==3):
        print(1)
        continue

    #loop through until finds the disparity
    for j in range (1,len(x)):
        if(x[j]+1!=x[j+1]):
            print(j+1)
            break
