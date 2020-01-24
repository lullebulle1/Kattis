#for each line, put it into an array and if the first words are
#simon says, then print the rest of the array
for i in range(0,int(input())):
    words = input().split(' ')
    if(words[0] == "Simon" and words[1]=="says"):
        print(' '.join(words[2:]))
