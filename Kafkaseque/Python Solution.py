arr = []
for i in range(int(input())):
    arr.append(int(input()))

count = 0
low = -1
while (arr.count(101) != len(arr)):
    posLow = -1
    while(min(arr)!=101 and arr.index(min(arr))>posLow):
        low = min(arr)
        posLow = arr.index(low)
        arr[posLow]=101

    count+=1
print(count)
