height, width = list(map(int, input().split(' ')))

street = []
out = [0,0,0,0,0]
for i in range(height):
    street.append(input())

for row in range(height-1):
    for col in range(width-1):
        spots = [street[row][col],street[row+1][col],street[row][col+1],street[row+1][col+1]]
        if("#" not in spots):
            out[spots.count("X")]+=1

for i in out:
    print(i)
