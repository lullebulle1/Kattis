for i in range(int(input())):
    guests = int(input())
    guestList = list(map(int,input().split(' ')))
    print("Case #{}:".format(i+1),[x for x in guestList if guestList.count(x)!=2][0])
