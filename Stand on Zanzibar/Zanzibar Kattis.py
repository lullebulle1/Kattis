for i in range(int(input())):
    imports = 0
    year = list(map(int,input().split(' ')))
    for j in range(len(year)):
        if(year[j+1] ==0):
            break
        if(year[j+1]>year[j]*2):
            imports+=year[j+1]-year[j]*2
    print(imports)
