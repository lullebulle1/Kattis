sheets, amount = list(map(int, input().split()))

count = amount - sheets%amount
rollsneed = 1
if (sheets%count == 0):
    rollsneed = 0
while (sheets%count!=0):
    rollsneed += 1
    count = count - sheets%count
print (rollsneed+1)
