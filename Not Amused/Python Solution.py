import sys

#variables
day = 1
people = {}
peoplein = {}

#for every line
for line in sys.stdin:
    line = line.strip('\n')

    #if open, just skips
    if (line == "OPEN"):
        continue
    #prints everything and then resets
    elif (line == "CLOSE"):
        print ("Day {}".format(day))
        for i in sorted(people.keys()):
            print ("{0} ${1:.2f}".format(i, people[i]*0.1))
        people = {}
        day += 1
        print ()
    #adds to different dicts
    else:
        line = list(line.split())
        if (line[0] == "ENTER"):
            peoplein[line[1]] = int(line[2])
        else:
            if (line[1] in people.keys()):
                people[line[1]] = int(line[2]) - peoplein[line[1]] + people[line[1]]
            else: 
                people[line[1]] = int(line[2]) - peoplein[line[1]]
            peoplein.pop(line[1])
