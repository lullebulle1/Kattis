#fraction function
from fractions import Fraction

#takes in the input
numbrings = int(input())
radii = list(map(int, input().split(' ')))

#prints each fraction
for i in range(1,numbrings):
    x = str(Fraction(radii[0],radii[i]))
    print(x if "/" in x else "{}/{}".format(x,1))
