arr = list(map(int,input().split(' ')))

for i in range(arr[0]):
    output = ""
    inputs = input()
    for j in range(arr[1]):
        output+=inputs[j]*arr[3]
    print((output+"\n")*arr[2],end='')
