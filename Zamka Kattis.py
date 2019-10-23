minx, maxx, sumd = int(input()), int(input()), int(input())
outputarray = []

for i in range(minx, maxx+1):
    numb = list(str(i))
    tempsum = 0
    
    for j in range(0,len(numb)):
        tempsum += int(numb[j])
        
    if (tempsum == sumd):
        outputarray.append(i)

print(str(min(outputarray))+"\n"+str(max(outputarray)))
