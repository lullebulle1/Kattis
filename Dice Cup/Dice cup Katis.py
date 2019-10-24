array = list(map(int,input().split(' ')))
listfinal = [0] * (array[0]+array[1]+1)

for i in range (1, array[0]+1):
    for j in range (1, array[1]+1):
        listfinal[i+j] = listfinal[i+j]+1

high = [x for x, y in enumerate(listfinal) if y == max(listfinal)]
for z in high:
    print(z)

