from math import floor

#takes in the inputs into a sorted array
numbs = sorted([int(input()) for x in range(int(input()))], reverse=True)
sums = 0

#loops through groups of 3
for i in range(floor(len(numbs)/3)):
    sums += numbs[i*3] + numbs[i*3+1]

#adds all remaining books and then prints total price
sums += sum(numbs[3*floor(len(numbs)/3):])
print (sums)
