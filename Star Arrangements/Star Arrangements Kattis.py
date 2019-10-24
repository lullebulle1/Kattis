import math

stars = int(input())
print("{}:".format(stars))
for i in range(2,math.ceil(stars/2)+1):
    if(stars % (2*i-1) == i or stars % (2*i-1)==0):
        print("{},{}".format(i,i-1))
    if(stars % (2*i) == i or stars % (2*i)==0):
       print("{},{}".format(i,i))
