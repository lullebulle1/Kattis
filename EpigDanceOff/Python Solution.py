x, y = list(map(int, input().split()))

#takes in input
arr = []
for i in range (x):
    arr.append(input())

#finds the empty columns between moves
count = 1
for j in range (y):
    line = [arr[i][j] for i in range(x) if arr[i][j] != "_"]
    if (len(line) == 0):
        count += 1

print (count)
