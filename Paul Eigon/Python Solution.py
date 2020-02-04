#imports floor
from math import floor

#takes in input
N, P, Q = list(map(int, input().split(' ')))

#prints the answer (Add the two scores, divide by games per player
#and then mod 2 to decide if paul or opponent. Floor it just in case
print("paul" if floor((P+Q)/N)%2==0 else "opponent")

