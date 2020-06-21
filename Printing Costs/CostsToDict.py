import sys

#takes in the input of costs and creates a python dictionary
mydict = {}
for line in sys.stdin:
    x = line.split("        ")
    for i in x:
        mydict[i[0]] = int(''.join(i[2:]))
print (mydict)
