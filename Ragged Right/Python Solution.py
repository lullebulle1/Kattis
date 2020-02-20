import sys

#takes in all input
lineLens = []
for line in sys.stdin:
    x = line.replace('\n','')
    lineLens.append(len(x))

#calculates the max line length
maxLen = max(lineLens)
count = 0

#calculates raggedness score for all lines except the last one
for i in range(0,len(lineLens)-1):
    count += (lineLens[i]-maxLen)**2

#prints output
print(count)
