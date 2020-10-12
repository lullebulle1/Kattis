#takes in inputs
x = int(input())
bricks = list(map(int, input().split()))
count = 1

#loops through to find a new tower
for i in range (x-1):
    if (bricks[i] < bricks[i+1]):
        count = count + 1

#prints answer
print (count)
