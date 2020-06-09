abc = list(map(int, input().split()))
abc.sort()
order = list(input())

for i in order:
    print (abc[ord(i)%65], end=' ')
print ()
