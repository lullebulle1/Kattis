from math import floor

#fills array with 3s and 0s, 3 represents a folded
counts, players = list(map(int, input().split(' ')))
arr = [3 if x%2==0 else 0 for x in range(players*2)]

#goes through until only 1 is left
index = 0
while (len([x for x in arr if x>0])>1):
    counted = 0
    while (counted != counts):
        #resets index to 0
        if (index>=players*2):
            index = index%(players*2)

        #skips any 0's
        if (arr[index] == 0):
            index += 1
        #calculations if it is a 1 (palm)
        elif (arr[index] == 1):
            if (counted == counts-1):
                arr [index] = 0
            index += 1
            counted += 1
        #calculations if it is a 2 (fist)
        elif (arr[index] == 2):
            if (counted == counts-1):
                arr[index] = 1
            index += 1
            counted += 1
        #calculations if it is a 3 (folder hands)
        elif (arr[index] == 3):
            if (counted == counts-1):
                arr[index] = 2
                arr [index+1] = 2
            else:
                index += 2
            counted += 1

#finds the index in the array and prints what player that belongs to
print (1 + floor([idx for idx, val in enumerate(arr) if val != 0][0]/2.0))
