for i in range(int(input())):
    day, month = list(map(int, input().split()))
    di = list(map(int, input().split()))

    howmany = 0
    currday = 0
    #goes through every month and sees if the 13th falls on a friday
    for j in range(month):
        if (di[j] >= 13 and (currday+13)%7==6):
            howmany += 1
        currday += di[j]
    print(howmany)
