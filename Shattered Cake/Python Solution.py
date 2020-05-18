width = int(input())
numb = int(input())

totarea = 0
for i in range(numb):
    x, y = list(map(int, input().split(' ')))
    totarea += x*y

print(int(totarea/width))
