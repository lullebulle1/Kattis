#takes in the input
word = list(input())
guesses = list(input())

#i is the number of incorrect guess, arrLoc is just total guesses
i = 0
arrLoc = 0

#while the number of incorrect guesses is not 10
while(i<10):
    #if it was incorrect, add 1 to incorrect
    if(guesses[arrLoc] not in word):
        i+=1

    #delete the letter from the word array
    word = [x for x in word if x != guesses[arrLoc]]
    arrLoc += 1

#if the word array is empty, you won otherwise lost
print("WIN" if len(word)==0 else "LOSE")
    
