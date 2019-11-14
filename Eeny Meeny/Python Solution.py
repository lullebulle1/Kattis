count = len(input().split(' '))
players, a, b = [], [], []
teamA = True
for i in range(int(input())):
    players.append(input())

index = (count-1)%len(players)
while len(players)>0:
    if teamA:
        a.append(players.pop(index))
    else:
        b.append(players.pop(index))

    if(len(players)==0):
        break
    
    teamA = not teamA
    index = ((index+count)%len(players))-1
    if(index<0):
        index = len(players)-1

print(len(a),'\n','\n'.join(a),sep='')
print(len(b),'\n','\n'.join(b),sep='')
