arr = list(map(int,input().split(' '))) #length of sides, distance right, distance down

box1 = arr[1]*arr[2]*4 #top left
box2 = (arr[0]-arr[1])*(arr[0]-arr[2])*4 #bottom right
box3 = (arr[0]-arr[1])*arr[2]*4 #top right
box4 = arr[1]*(arr[0]-arr[2])*4 #bottom left

print(max(box1,box2,box3,box4))
