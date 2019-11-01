numb = int(input())

while True:
    numbList = list(str(numb))
    tot = 0
    for i in range(len(numbList)):
        tot+=int(numbList[i])

    if(numb%tot == 0):
        break
    numb+=1

print(numb)
