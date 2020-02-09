#needed for sqrt function
from math import sqrt

#takes in input
arr = []
arr.append(list(map(int, input().split(' '))))
arr.append(list(map(int, input().split(' '))))
arr.append(list(map(int, input().split(' '))))

#goes through each number
count = 0
for i in range(1,9):
    #saves the integer as a point
    indexI = []
    indexI2 = []

    #saves the point of the number and next number
    for j in range(3):
        if (i in arr[j]):
            indexI = [j,arr[j].index(i)]
        if ((i+1) in arr[j]):
            indexI2 = [j,arr[j].index(i+1)]

    #finds distance between the two points
    count += sqrt((indexI2[0]-indexI[0])**2 + (indexI2[1]-indexI[1])**2)

#prints the count
print(round(count,10))
