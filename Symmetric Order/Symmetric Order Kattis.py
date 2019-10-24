x = 1

def recur (i):
    if (i>=howmany):
        return ""
    elif (i==howmany-1):
      return names[i]+"\n"
    return names[i]+"\n" + recur(i+2) + names[i+1]+"\n"

while True:
    howmany = int(input())
    if (howmany==0):
        break
    names = []
    for i in range(howmany):
        names.append(str(input()))
    
    print("SET",x)
    print(recur(0),end='')
    x+=1
    
