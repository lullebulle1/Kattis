A, B, C = list(map(int,input().split(' ')))

truck1 = list(map(int,input().split(' ')))
truck2 = list(map(int,input().split(' ')))
truck3 = list(map(int,input().split(' ')))

x = min(truck1[0], truck2[0], truck3[0])
y = max(truck1[1], truck2[1], truck3[1])

cost = 0

for i in range (x,y):
    count = 0
    if(truck1[0]<=i and i<=truck1[1]):
        count+=1
    if(truck2[0]<=i and i<=truck2[1]):
        count+=1
    if(truck3[0]<=i and i<=truck3[1]):
        count+=1
        
    print(i, count)

    cost += A if count==1 else 2*B if count==2 else 3*C if count==3 else 0

print(cost)
