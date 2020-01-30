#takes in the line and calculates its size/2
message = input()
lenMes = int(len(message)/2)

#converts the message to numbers and halves it
firstPart = [ord(x)%65 for x in message[0:lenMes]]
secondPart = [ord(x)%65 for x in message[lenMes::]]


#calculates the sum of both lists
sumFirst = sum(firstPart)%26
sumSecond = sum(secondPart)%26

#adjusts the arrays to realign them
firstPart = [(x+sumFirst)%26 for x in firstPart]
secondPart = [(x+sumSecond)%26 for x in secondPart]

#does the final adjustments to each character and then prints them all
print(''.join([chr((firstPart[i]+secondPart[i])%26+65) for i in range (0, lenMes)]))

