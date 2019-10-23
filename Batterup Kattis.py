totalHits = int(input())
finalHits = totalHits
total = 0
hits = list(map(int,input().split(' ')))

for i in range(0,totalHits):
    if (hits[i]<0):
        finalHits-=1
    else:
        total+=hits[i]
print(float(total)/finalHits)
