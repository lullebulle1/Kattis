import sys

#a dictionary of all possible combinations
morseDict = {
        "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.",
        "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.",
        "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-",
        "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", 
        "_":"..--", ",":".-.-", ".":"---.", "?":"----"
        }

#for each line of input
for line in sys.stdin:
    #creates a list of all the elements, converting to morse code
    messageMorse = [morseDict[x] for x in list(line.strip())]

    #creates a list of the length of each elements, and reverses it
    messageSize = [len(x) for x in messageMorse][::-1]

    #creates a string based on the message encoded above
    newMessage = ''.join(messageMorse)

    #goes through each chunk based on the reversed messageSize list
    letterLen  = 0
    for i in messageSize:
        #finds the letter in the dictionary and prints it
        letter = newMessage[letterLen:letterLen+i]
        print(list(morseDict.keys())[list(morseDict.values()).index(letter)], end='')
        letterLen += i

    #adds a new line space
    print()
