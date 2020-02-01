#the list of letters on each key
charArr = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

#goes through each input
for i in range(int(input())):
    #takes in that lines input
    strIn = list(input())
    
    #prints the first part of the answer
    print("Case #{}: ".format(i+1),end='')

    #keeps track of previous number 
    prevChar = -1

    #for each letter in the input 
    for x in strIn:
        #checks to see if its a space and adds 0
        if(x==' '):
            if(prevChar==0):
                print(' ',end='')

            print(0,end='')
            prevChar = 0
            continue

        #calculates the index of the character and adds 2
        index = [idx for idx, s in enumerate(charArr) if x in s][0] + 2
        
        #adds space if matched with previous numbers pressed
        if(prevChar==index):
            print(' ',end='')
        
        #prints the index #'s of times equal to location of the char in the string
        print(str(index) * (list(charArr[index-2]).index(x)+1), end='')

        #sets the prev char to number
        prevChar = index

    #adds new line
    print()

