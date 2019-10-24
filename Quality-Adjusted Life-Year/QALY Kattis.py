total = 0
for i in range (0, int(input())):
    array = input().split(' ')
    total += float(array[0]) * float(array[1])
print(total)
