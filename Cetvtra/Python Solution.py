point1, point2 = [], []
for i in range(3):
    arr = list(map(int,input().split(' ')))
    point1.append(arr[0])
    point2.append(arr[1])
    
print([y for y in point1 if point1.count(y)==1][0],[y for y in point2 if point2.count(y)==1][0])

