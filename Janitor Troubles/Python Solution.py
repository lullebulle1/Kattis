import math

#Max Area = sqrt((S-a) * (S-b) * (S-c) * (S-d))
#where S = (a + b + c + d)/2

a, b, c, d = list(map(int, input().split(' ')))
sp = (a+b+c+d)/2

print(math.sqrt((sp-a)*(sp-b)*(sp-c)*(sp-d)))

