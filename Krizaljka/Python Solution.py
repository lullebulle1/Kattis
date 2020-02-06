#takes in the two words
wordX, wordY = input().split(' ')

#indexs of the first element found
locX = 0
locY = 0

#finds the first element from wordX that is in wordY
for i in wordX:
    if (i in wordY):
       locX = wordX.index(i)
       locY = wordY.index(i)
       break

#goes through the 2x2 matrix and prints characters
for x in range(len(wordY)):
    if(x==locY):
        print(wordX) 
        continue

    for y in range(len(wordX)):
        print("." if y!=locX else wordY[x], end='')
    
    print()
