for i in range(0,int(input())):
    array = input().split(' ')
    b = int(array[0])
    p = float(array[1])
    answer = 60*b/p
    print(answer-60/p,answer,answer+60/p)
