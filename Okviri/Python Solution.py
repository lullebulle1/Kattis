x = list(input())
y = len(x)

#prints the first row
for i in range(y):
    print("..*." if i%3==2 and i != 0 else "..#.",end='')
print(".")

#prints the second row
for i in range(y):
    print(".*.*" if i%3==2 and i != 0 else ".#.#",end='')
print(".")

#prints the middle row
for i in range(y):
    print("{}.{}.".format("*" if (i!=0 and i%3==2) or (i!=0 and i%3==0) else "#",x[i]),end='')
print("*" if y%3==0 else "#")

#prints the second to last row
for i in range(y):
    print(".*.*" if i%3==2 and i != 0 else ".#.#",end='')
print(".")

#prints the last row
for i in range(y):
    print("..*." if i%3==2 and i != 0 else "..#.",end='')
print(".")

