m, n = list(map(int, input().split()))
u, l, r, d = list(map(int, input().split()))

words = []
for i in range (m):
    words.append(input())

#handles the upper bounds
count = 0
for upper in range (u):
    for row in range(n+l+r):
        print ("#" if (upper+row)%2==0 else ".", end='')
    print()
    count += 1

#handles the middle
for word in range(m):
    for row in range(l):
        print ("#" if (count+row)%2==0 else ".", end='')
    print (words[word], end='')
    for row in range(r):
        print ("#" if (count+n+row)%2==0 else ".", end='')
    print()
    count += 1
        
#handles the bottom
for upper in range (d):
    for row in range(n+l+r):
        print ("#" if (count+row)%2==0 else ".", end='')
    print()
    count += 1
