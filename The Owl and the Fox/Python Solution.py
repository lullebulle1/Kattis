def sumdigits(x):
    tmp = list(str(x))
    tmpout = 0
    for k in tmp:
        tmpout += int(k)
    return tmpout

for i in range(int(input())):
    inp = int(input())
    sums = sumdigits(inp)
    if (sums == 1):
        print (0)
        continue
    
    for j in range (inp, 0, -1):
        if (sumdigits(j) < sums):
            print (j)
            break
