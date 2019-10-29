days = int(input())
arr = list(map(int,input().split(' ')))
minVal = min(arr)

for i in range(days):
    if (arr[i] == minVal):
        print(i)
        break
