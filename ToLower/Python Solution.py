P, T = list(map(int,input().split(' ')))

#loops through the questions
count = 0
for i in range(P):
    succ = True
    for j in range(T):
        #if it finds a string that's upper case, don't add one to count
        word = input()
        if (not word[1:].islower()):
            succ=False
    count += 1 if succ else 0

#prints the count of correct
print(count)
