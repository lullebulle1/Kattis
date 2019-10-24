while True:
    times = int(input())
    if (times==-1):
        break;
    
    elapsedTime = 0
    output = 0
    for i in range(times):
        arr = list(map(int,input().split(' ')))
        output += arr[0]*(arr[1]-elapsedTime)
        elapsedTime=arr[1]

    print(output,"miles")
