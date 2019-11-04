scores = input()
a, b = 0, 0

for i in range(0,len(scores),2):
    if scores[i]=="A":
        a+=int(scores[i+1])
    else:
        b+=int(scores[i+1])

print("A" if a>b else "B")

