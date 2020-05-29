for i in range(int(input())):
    r, p, d = list(map(int, input().split()))

    arr = []
    fullport = 0
    for j in range(r):
        tmp = list(input().split())
        if (tmp[2] == "100.0"):
            fullport = float(tmp[1])*(d/p)

        arr.append(tmp)

    print ("Recipe # {0}".format(i+1))
    for k in range(r):
        print ("{0} {1:.1f}".format(arr[k][0], fullport * float(arr[k][2])/100))
    print ("-"*40)
