from sys import stdin

#variables
mydict = {}
foundline = False

#takes in every line
for line in stdin:
    #decides if blank line was found
    if (len(line) == 1):
        foundline = True
        continue
    
    #either prints or adds to dictionary
    outline = list(line.split())
    if (foundline):
        line = line.strip('\n')
        print (mydict[line] if line in mydict.keys() else "eh")
    else:
        mydict[outline[1]] = outline[0]
