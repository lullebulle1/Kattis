#variables
prev = 0
count = 1

#if the next input is ever smaller, we know we need to
#do it once more, so keeps track of that for all inputs
for i in range(int(input())):
    x = int(input())
    if(x<prev):
        count+=1
    
    prev = x
print(count)
