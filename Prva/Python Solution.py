#takes in input and inits variables
R, C = list(map(int, input().split(' ')))
arr = []
words = []

#takes in input and adds words to words list
for i in range(R):
    arr.append(input())
    x = arr[i].split("#")
    for k in x:
        if (k!='' and len(k)>1):
            words.append(k)

#checks the columns and adds to words list
for j in range(C):
    x = ""
    for k in range(R):
        x += arr[k][j]

    y = x.split("#")
    for l in y:
        if (l!='' and len(l)>1):
            words.append(l)

#sorts list and prints the first word
words.sort()
print(words[0])
