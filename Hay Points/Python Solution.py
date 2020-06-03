m, n = list(map(int, input().split()))
mydict = {}

for i in range(m):
    desc, mon = list(input().split())
    mydict[desc] = int(mon)

for j in range(n):
    money = 0
    while True:
        x = list(input().split())
        if (len(x) == 1 and x[0] == "."):
            print(money)
            break
        money += sum(map(lambda l: mydict[l], filter(lambda k: k in mydict.keys(), x)))
