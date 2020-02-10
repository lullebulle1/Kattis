#takes in input
r, s, k = list(map(int, input().split(' ')))
window = [input() for x in range(r)]

#variable declaration
spotMost = [0,0]
count = 0

#loops through the entire window
for row in range(r-k+1):
    for col in range(s-k+1):
        tempCount = 0
        #loops through the space enclosed by the racket and counts how many flies
        for spoty in range(1,k-1):
            for spotx in range(1,k-1):
                if(window[row+spoty][col+spotx] == "*"):
                    tempCount+=1

        #if there is more, change spotMost and count
        if(tempCount>count):
            count=tempCount
            spotMost = [row,col]

#prints the new array with the racket added to the window
print(count)
for row in range(r):
    for col in range(s):
        if((row==spotMost[0] or row==spotMost[0]+k-1) and (col==spotMost[1] or col==spotMost[1]+k-1)):
            print("+",end='')
        elif((row==spotMost[0] or row==spotMost[0]+k-1) and col in range(spotMost[1],spotMost[1]+k-1)):
            print("-",end='')
        elif((col==spotMost[1] or col==spotMost[1]+k-1) and row in range(spotMost[0],spotMost[0]+k-1)):
            print("|",end='')
        else:
            print(window[row][col],end='')
    print()
