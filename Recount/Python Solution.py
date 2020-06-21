people = {}

#takes in all input into a dictionary
x = input()
while (x != "***"):
    if (x in people.keys()):
        people[x] += 1
    else:
        people[x] = 1
    x = input()

#finds max votes and all people with those votes. Prints answer
maxvotes = max([people[y] for y in people.keys()])
outarr = [y for y in people.keys() if people[y]==maxvotes]
print ("Runoff!" if len(outarr)>1 else outarr[0])
