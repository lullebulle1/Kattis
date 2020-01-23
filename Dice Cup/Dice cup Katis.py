#takes in the two inputs and stores as array[0] and array[1]
array = list(map(int,input().split(' ')))

#creates a new array of the length of the two values + 1, all 0's
listfinal = [0] * (array[0]+array[1]+1)

#for every possible combination, add 1 to that spot in the array
for i in range (1, array[0]+1):
    for j in range (1, array[1]+1):
        listfinal[i+j] = listfinal[i+j]+1

#searched through the array and finds the highest values
high = [x for x, y in enumerate(listfinal) if y == max(listfinal)]

#prints all the highest values
for z in high:
    print(z)

