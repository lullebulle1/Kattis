string = list(input())
white = 0.0
lower = 0.0
upper = 0.0
symbol = 0.0
total = len(string)

for i in range(0,len(string)):
    if(string[i] == "_"):
        white+=1
    elif(string[i].islower()):
        lower+=1
    elif(string[i].isupper()):
        upper+=1
    else:
        symbol+=1

print(white/total)
print(lower/total)
print(upper/total)
print(symbol/total)
