x = int(input())
hits = list(map(int,input().split(' ')))
hits = [x for x in hits if x!=-1]

print(sum(hits)/len(hits))
