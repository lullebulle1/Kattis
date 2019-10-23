b = input()
print(len([x for x, a in enumerate(list(map(int,input().split(' ')))) if a<0]))
