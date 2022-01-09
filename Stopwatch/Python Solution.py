times = int(input())

if (times%2 == 1):
    print ("still running")
else:
    arr = [int(input()) for i in range(times)]
    totTime = 0
    for i in range(1, len(arr), 2):
        totTime += arr[i]-arr[i-1]

    print (totTime)
