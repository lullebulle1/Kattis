amount = int(input().split(' ')[1])
points = list(map(int,input().split(' ')))

for i in range(amount):
    inputs = list(map(int,input().split(' ')))
    if(inputs[0]==1):
        points[inputs[1]-1]=inputs[2]
    else:
        print(abs(points[inputs[1]-1]-points[inputs[2]-1]))
