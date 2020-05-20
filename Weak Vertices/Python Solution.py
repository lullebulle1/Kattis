def findtri(i, arr2):
    #finds all indexes of 1's in a given row
    locs = [y for y in range(len(arr2[i])) if arr2[i][y] == 1]

    #goes through each found 1 and see if it has an edge with another 1 in the same row
    for j in range(len(locs)):
        for k in range(j, len(locs)):
            if (arr2[locs[j]][locs[k]] == 1):
                return [i, locs[j], locs[k]]

    #returns empty if nothing found
    return []

x = int(input())
while (x != -1):
    arr = []
    output = [] 
    checked = []

    #takes in the arr
    for i in range(x):
        arr.append(list(map(int,input().split())))

    #goes through the arr
    for i in range(x):
        if(arr[i].count(1) >= 2 and i not in checked):
            [checked.append(y) for y in findtri(i, arr)] 

    #finds everything not found and prints it
    output = [str(y) for y in range(x) if y not in checked]
    print(' '.join(output))
    
    x = int(input())
