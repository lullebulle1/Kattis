#takes in the cost per truck
A, B, C = list(map(int,input().split(' ')))

#takes in the time interval of each truck
truck1 = list(map(int,input().split(' ')))
truck2 = list(map(int,input().split(' ')))
truck3 = list(map(int,input().split(' ')))

#finds the minimum start time and max stop time
x = min(truck1[0], truck2[0], truck3[0])
y = max(truck1[1], truck2[1], truck3[1])

#intialize cost variable
cost = 0

#for each minute within the max time interval
#if a truck is parked at that time, add to count
for i in range (x,y+1):
    count = 0
    if(truck1[0]<=i and i<truck1[1]):
        count+=1
    if(truck2[0]<=i and i<truck2[1]):
        count+=1
    if(truck3[0]<=i and i<truck3[1]):
        count+=1
    
    #adds to cost based on number of trucks parked (count var)
    cost += A if count==1 else 2*B if count==2 else 3*C if count==3 else 0

#prints out the entire cost
print(cost)
