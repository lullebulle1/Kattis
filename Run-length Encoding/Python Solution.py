prob, word = list(input().split())
output = ""

if (prob == "E"):
    count = 1
    prevchr = word[0]
    for i in word[1:]:
        if (i == prevchr):
            count += 1
        else: 
            output += prevchr + str(count)
            prevchr = i
            count = 1

    output += prevchr + str(count)
elif (prob == "D"):
    for i in range(0, len(word), 2):
        output += word[i]*int(word[i+1])

print (output)
