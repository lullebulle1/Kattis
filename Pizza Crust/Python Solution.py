#needed for pi
from math import pi

#scans in the two numbers
rad, crust = list(map(int,input().split(' ')))

#calculates the entire radius as well as just the inner area
fullArea = pi*rad**2
innerArea = pi*(rad-crust)**2

#prints out the percentage that is cheese
print(100*innerArea/fullArea)
