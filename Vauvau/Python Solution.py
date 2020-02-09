A, B, C, D = list(map(int, input().split(' ')))
men = list(map(int, input().split(' ')))

for i in range(3):
    span = 0
    count = 0
    safe = 0
    while(span<men[i]):
        if(count%2==0):
            span+=A
        else:
            span+=B
        count+=1
        
    if(count%2==1):
        safe+=1

    count = 0
    span = 0
    while(span<men[i]):
        if(count%2==0):
            span+=C
        else:
            span+=D
        count+=1
        
    if(count%2==1):
        safe+=1

    print("none" if safe==0 else "one" if safe==1 else "both")
