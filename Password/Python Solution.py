#takes in the input into an array
arr = []
for i in range(int(input())):
    tmp = list(input().split())
    arr.append(float(tmp[1]))

#sorts the array
arr.sort(reverse=True)
sums = 0

#adds probability*position in array
for j in range (len(arr)):
    sums += arr[j]*(j+1)

#prints answer
print (sums)
