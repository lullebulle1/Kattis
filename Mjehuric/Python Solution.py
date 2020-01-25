#takes in input
arr = list(map(int, input().split(' ')))
i = 0

#while it isn't the correct array
while(arr!=[1,2,3,4,5]):
    #swaps elements if the left one is greate
    if(arr[i]>arr[i+1]):
        arr[i], arr[i+1] = arr[i+1], arr[i]
        print(*arr)
    
    #incriments i if it isn't out of range
    i = i+1 if i+1<4 else 0
