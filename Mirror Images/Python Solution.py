#For each test case
for i in range(int(input())):
    #takes in the number of cases in this case
    x, y = list(map(int,input().split(' ')))

    #adds each string to an array
    arr = []
    for j in range(x):
        arr.append(input())

    #prints the test # and the reversed array of reversed strings
    print("Test",i+1)
    print('\n'.join([z[::-1] for z in arr][::-1]))
