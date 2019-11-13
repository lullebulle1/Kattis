dates = []
for i in range(int(input())):
    x, y = input().split(' ')
    dates.extend([z for z in range(int(x),int(y)+1) if z not in dates])
print(len(dates))
