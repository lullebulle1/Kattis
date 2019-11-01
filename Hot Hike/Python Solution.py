i, days, whichDay = 0, int(input()), 1
inputs, largest = list(map(int, input().split(' '))), [41,41]

while i < days-2:
    if (inputs[i] < max(largest) and inputs[i+2] < max(largest)):
        largest = [inputs[i],inputs[i+2]]
        whichDay=i+1
    i+=1
print(whichDay, max(largest))
    
