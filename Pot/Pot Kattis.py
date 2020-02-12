total = 0;
for i in range(int(input())):
    x = input()
    total += int(x[0:len(x)-1])**int(x[len(x)-1])

print(total)
