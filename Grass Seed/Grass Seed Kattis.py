total = 0.0
cost = float(input())

for i in range (0, int(input())):
    array = list(map(float,input().split(' ')))
    total += array[0]*array[1]*cost

print(total)
