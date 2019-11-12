from math import floor

while True:
   inputs = list(map(int, input().split(' ')))
   if(inputs[0]==0):
       break

   print(floor(inputs[0]/inputs[1]), inputs[0]%inputs[1], "/", inputs[1])
