numb = int(input())

for i in range(numb):
    setnumb, ints = list(map(int, input().split(' ')))

    #calculate S1
    s1 = 0
    for i in range(1, ints+1):
        s1 += i

    #calculate S2
    s2 = 0
    for i in range(1, 2*(ints), 2):
        s2 += i

    #calculate S3
    s3 = 0
    for i in range(2, 2*(ints+1), 2):
        s3 += i

    print ("{} {} {} {}".format(setnumb, s1, s2, s3))
