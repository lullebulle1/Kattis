parts, days = list(input().split(' '))
partList = []

for i in range(int(days)):
    inp = input()
    if (inp not in partList):
        partList.append(inp)
    
    if (len(partList) == int(parts)):
        print(i+1)
        break
    
if(len(partList) != int(parts)):
    print("paradox avoided")