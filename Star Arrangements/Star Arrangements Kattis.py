#uses the ceil function from math
from math import ceil

#takes in inputs and pritns it back out
stars = int(input())
print("{}:".format(stars))

#for each possible stars in a row, from 2 to half the given amount
for i in range(2,ceil(stars/2)+1):
    #check to see if the row and the next row (i-1) are able to evenly
    #divide into the arrangement. This does this by checking if it evenly
    #does so with % = 0 or if its a multiple of the original row.
    if(stars % (2*i-1) == i or stars % (2*i-1)==0):
        print("{},{}".format(i,i-1))

    #does the same but with the rows being the same number
    if(stars % (2*i) == i or stars % (2*i)==0):
       print("{},{}".format(i,i))
