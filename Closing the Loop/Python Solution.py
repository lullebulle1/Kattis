for i in range(1,int(input())+1):
    numb = int(input())
    ropes = list(input().split(' '))
    length = 0

    b = [int(x[:-1]) for x in ropes if "B" in x]
    r = [int(x[:-1]) for x in ropes if "R" in x]

    b.sort(reverse=True)
    r.sort(reverse=True)

    for j in range(min(len(b),len(r))):
        length += b[j] + r[j] - 2

    print("Case #{}: {}".format(i,length))
