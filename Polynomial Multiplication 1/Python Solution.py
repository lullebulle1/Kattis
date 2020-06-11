#for each test case
for i in range(int(input())):
    #first number set
    ord1 = int(input())
    numb1 = list(map(int, input().split()))

    #second number set
    ord2 = int(input())
    numb2 = list(map(int, input().split()))

    #creates the matrix and output
    arr = [[y*x for y in numb1] for x in numb2]
    out = [0 for l in range(ord1+ord2+1)]

    #adds the sum of each to appropriate output
    for j in range(ord2+1):
        for k in range(ord1+1):
            out[j+k] += arr[j][k]

    #prints answer
    print (ord1+ord2)
    print (' '.join([str(m) for m in out]))
