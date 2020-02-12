import math

#calculates the hypotenuse and checks if the match falls within that
numb, a, b = list(map(int,input().split(' ')))
c = math.sqrt(a**2+b**2)

for i in range(0,numb):
    print("DA" if int(input())<=c else "NE")
