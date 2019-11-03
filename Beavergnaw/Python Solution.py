import math 
while True:
    arr = list(map(int,input().split(' ')))
    if(arr[0]==0):
        break;
    print((arr[0]**3-6*arr[1]/math.pi)**(1/3))

    
#(D^3 - 6V/π)^(1/3)
