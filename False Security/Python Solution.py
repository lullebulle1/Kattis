import sys

#The array of all the given morse codes
morseArr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

#goes through each input
for line in sys.stdin:
    #cleans input and ends loop as backup
    messageMorse = list(line.strip())
    if (len(messageMorse)==0):
        break
    
    #goes through each letter and transforms into morse
    for i in range(0,len(messageMorse)):
        if(messageMorse[i] == "_"):
            messageMorse[i] = "..--"
        elif(messageMorse[i] == ","):
            messageMorse[i] = ".-.-"
        elif(messageMorse[i] == "?"):
            messageMorse[i] = "----"
        elif(messageMorse[i] == "."):
            messageMorse[i] = "---."
        else:
            messageMorse[i] = morseArr[ord(messageMorse[i])%65]

    #calculates the length of each letter as morse, then reverses the list
    messageLength = [len(x) for x in messageMorse][::-1]
    
    #creates a plain string of the message
    newMessage = ''.join(messageMorse)
   
    #goes through the entire message
    i, count = 0,0 
    while i<len(newMessage):
        #finds the new letter based on the length array
        letter = newMessage[i:i+messageLength[count]]

        #calculates the new letter and prints that letter
        if (letter in morseArr):
            print(chr(morseArr.index(letter)+65), end='')
        elif(letter == "..--"):
            print("_", end='')
        elif(letter == ".-.-"):
            print(",", end='')
        elif(letter == "----"):
            print("?", end ='')
        elif(letter == "---."):
            print(".", end='')
        
        #increases count (where in messageLength array) and i (where to start in the message)
        i+=messageLength[count]
        count+=1

    #adds a newline at the end
    print()
