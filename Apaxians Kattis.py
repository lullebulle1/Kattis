name = list(input())
prevLetter = name[0]
output = name[0]

for i in range(1, len(name)):
    if(name[i]!=prevLetter):
        output+=name[i]
        prevLetter=name[i]
print(output)
