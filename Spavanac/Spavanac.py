arr = list(map(int,input().split(' '))) #hours, min

arr[1]-=45
#using ternarys. Probably not the best way
arr[0] = arr[0]-1 if arr[1]<0 else arr[0]
arr[0] = 23 if arr[0]<0 else arr[0]
arr[1] = arr[1]+60 if arr[1]<0 else arr[1]

print(arr[0], arr[1])
