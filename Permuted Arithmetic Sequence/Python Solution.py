for i in range(int(input())):
    arr = list(map(int, input().split()))
    x = arr.pop(0)
    
    #sees if all diffs are the same
    dif = arr[1]-arr[0]
    fail = False
    for i in range(1,x-1):
        if (dif != arr[i+1]-arr[i]):
            fail = True
            break

    if (not fail):
        print ("arithmetic")
        continue

    #sees if all sorted diffs are the same
    arr.sort()
    dif = arr[1]-arr[0]
    fail = False
    for i in range(1,x-1):
        if (dif != arr[i+1]-arr[i]):
            fail = True
            break

    if (not fail):
        print ("permuted arithmetic")
        continue

    print ("non-arithmetic")
