import sys

#takes in the input and puts it in an array
arr = []
for line in sys.stdin:
    arr = arr + line.split(' ')

#strips any \n's in it
arr = [x.replace("\n",'') for x in arr]

#creates possible words and adds unique to a list
out = []
for i in range(len(arr)):
    for j in range(len(arr)):
        if(i!=j):
            word = arr[i]+arr[j]
            if(word not in out):
                out.append(word)

#sorts the list and prints the result
out.sort()
for i in out:
    print(i)
