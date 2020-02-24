def findHundred():
    for i in range(8):
        for j in range(i+1,9):
            if (count-x[i]-x[j]==100):
                return [i,j]

x = [int(input()) for i in range(9)]
count = sum(x)
places = findHundred()

for i in range(9):
    if(i not in places):
        print(x[i])
