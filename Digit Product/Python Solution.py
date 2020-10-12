#takes in input and casts to an array
x = input()
arr = [int(y) for y in x if y!='0']

#loops through until array is only 1 long
while (len(arr)!=1):
    numb = 1
    for i in arr:
        numb = numb * i

    arr = [int(y) for y in str(numb) if y!='0']

print (arr[0])
