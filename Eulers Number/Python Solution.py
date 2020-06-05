import math

inp = int(input())
sums = 0

if (inp>17):
    print (math.e)
else:
    for i in range (inp+1):
        sums += 1/math.factorial(i)
    print (sums)
