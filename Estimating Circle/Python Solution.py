#imports pi
from math import pi

#for every input case
while True:
    #saves the input as float variables
    r, m, c = list(map(float, input().split(' ')))

    #ends if it scans in the end case of 0
    if(r==0):
        break

    #calculates the answer
    print(round(pi*r**2, 9), round((c/m)*(2*r)**2,9))
