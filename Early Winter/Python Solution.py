n, dm = list(map(int, input().split()))
arr = list(map(int, input().split()))

loc = -1
for i in arr:
    if (i <= dm):
        loc = arr.index(i)
        break

if (loc != -1):
    print (f"It hadn't snowed this early in {loc} years!")
else:
    print ("It had never snowed this early!")
