while True:
    N = int(input())
    sumN = sum(list(map(int,list(str(N)))))
    p = 11
    if(N==0):
        break

    while(sum(list(map(int,list(str(N*p)))))!=sumN):
        p+=1

    print(p)
