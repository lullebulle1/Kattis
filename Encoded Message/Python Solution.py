import math
for i in range(int(input())):
    message = input()
    messageArr = []
    lenMess = int(math.sqrt(len(message)))
    output = []

    for j in range(lenMess):
        messageArr.append(list(message[j*lenMess:(j+1)*lenMess]))

    for x in range(lenMess-1,-1,-1):
        for y in range(lenMess):
            output.append(messageArr[y][x])

    print(''.join(output))
