for i in range(int(input())):
    x = list(map(int, input().split()))
    print (sum(x[1::])-x[0]+1)
