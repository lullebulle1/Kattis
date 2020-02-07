import sys

count = 1
for line in sys.stdin:
    #prints the case #
    print("Case {}: ".format(count),end='')
    earth, mars = list(map(int,line.split(' ')))

    #calculates the difference until earth hits the peak
    diffEarth = (365-earth)%365
    
    #how many reps in the next loop
    times=0

    #while initial mars input + the offset + earth multiples hits 0
    while((mars+365*times+diffEarth)%687!=0):
        times+=1

    #print the amount of times in loop * earth year + offset
    print((times)*365+diffEarth)

    count+=1
