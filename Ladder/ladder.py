import math
inputs = list(map(int,input().split(' '))) #hypotenuse, angle

print(int(math.ceil(inputs[0]/math.sin(inputs[1]*math.pi/180))))
