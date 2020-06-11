import sys

for line in sys.stdin:
    x = list(line.split())
    out = []
    for i in x:
        if (i[0] in "aeiouy"):
            out.append(i+"yay")
        else:
            tmp = list(i)
            while (not tmp[0] in "aeiouy"):
                tmp.append(tmp.pop(0))
            out.append(''.join(tmp)+"ay")
    print (' '.join(out))
