#takes in first line of input
totLength, divs = list(map(int,input().split(' ')))

#takes in the dividers, and adds 0 to beginning and totLength to end
lengths = list(map(int,input().split(' ')))
lengths.insert(0,0)
lengths.append(totLength)

#the output list
out = []

#goes through each element, and calculates distances from that
for i in range(divs+2):
    for j in range(i+1,divs+2):
        dist = lengths[j]-lengths[i]
        if(dist not in out):
            out.append(dist)

#sorts output and prints it
out.sort()
print(' '.join(list(map(str,out))))
