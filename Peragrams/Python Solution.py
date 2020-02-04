#takes in the word
word = list(input())

#previous letters in the array
prevGuesses = []

#how many excess letters
excess = 0

#for each letter, if not in prevGuesses add the excess of the count%2
for x in word:
    if (x not in prevGuesses):
        excess += word.count(x)%2
        prevGuesses.append(x)

#print the excess characters above 1
print(excess-1 if excess>1 else 0)
