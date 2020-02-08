cases = int(input())

for i in range(cases):
    inp = int(input())
    out = 0
    for j in range(inp):
        out = (out+.5)*2
    print(int(out))
