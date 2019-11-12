people = int(input())
pos = []

try:
    pos = list(map(int,input().split(' ')))
    print(1,' '.join([str(pos.index(x)+2) for x in range(people-1)]))
except:
    print(1)

