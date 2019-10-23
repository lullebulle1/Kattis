pos = [1,0,0]

for i in list(input()):
    if (i=="A"):
        pos[0], pos[1] = pos[1], pos[0]
    elif (i=="B"):
        pos[1], pos[2] = pos[2], pos[1]
    else:
        pos[0], pos[2] = pos[2], pos[0]

print(pos.index(1)+1)
