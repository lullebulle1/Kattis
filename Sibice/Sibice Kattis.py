import math

array = input().split(' ')

a = int(array[1])
b = int(array[2])
c = math.sqrt(a*a+b*b)

for i in range(0,int(array[0])):
    print("DA" if int(input())<c else "NE")
