init = list(map(int,input().split(' ')))
currpeople, denied = 0, 0

for i in range(init[1]):
    event = input().split(' ')

    if(event[0]=="leave"):
       currpeople -= int(event[1])
    elif(event[0] == "enter" and currpeople+int(event[1])<=init[0]):
        currpeople += int(event[1])
    else:
        denied += 1
print(denied)
