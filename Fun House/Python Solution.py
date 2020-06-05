x = input()

count = 1
while (x[0] != "0"):
    col, row = list(map(int, x.split()))

    startx = 0
    starty = 0
    arr = []

    for i in range(row):
        myrow = input()
        if ("*" in myrow):
            startx = myrow.index("*")
            starty = i 
        arr.append(list(myrow))

    #direc 1-up, 2-right, 3-down, 4-left 
    #sets initial direction
    direc = 0
    if (starty == 0):
        direc = 3
    elif (starty == row-1):
        direc = 1
    elif (startx == 0):
        direc = 2
    else:
        direc = 4

    #sets initials
    newx = startx
    newy = starty
    newchr = arr[newy][newx]

    #goes until wall
    while (newchr != 'x'):
        #add to direction
        if (direc == 1):
            newy -= 1
        elif (direc == 2):
            newx += 1
        elif (direc == 3):
            newy += 1
        elif (direc == 4):
            newx -= 1
        newchr = arr[newy][newx]

        #changes direction based on obstacles
        if (newchr == '/'):
            if (direc == 1):
                direc = 2 
            elif (direc == 2):
                direc = 1
            elif (direc == 3):
                direc = 4
            elif (direc == 4):
                direc = 3
        elif (newchr == '\\'):
            if (direc == 1):
                direc = 4 
            elif (direc == 2):
                direc = 3
            elif (direc == 3):
                direc = 2
            elif (direc == 4):
                direc = 1

    #sets end character
    arr[newy][newx] = "&"

    #prints the output
    print ("HOUSE {}".format(count))
    for j in arr:
        print(''.join(j))
    count += 1

    x = input()
