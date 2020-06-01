import sys

for line in sys.stdin:
    x = list(map(int, line.split()))
    sumx = sum(x)
    for i in range(len(x)):
        if (x[i] == sumx-x[i]):
            print(x[i])
            break
