arr = list(map(int,input().split(' ')))

if (arr[0]==arr[1] and arr[0]!=0):
    print("Even",arr[0]*2)
elif (arr[0]!=arr[1]):
    print("Odd",2*max(arr))
else:
    print("Not a moose")
