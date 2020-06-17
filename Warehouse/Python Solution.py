#for each test case
for i in range(int(input())):
    names = {}

    #takes everything into a dictionary
    for j in range(int(input())):
        x = list(input().split())
        if (x[0] not in names.keys()):
            names[x[0]] = int(x[1])
        else:
            names[x[0]] += int(x[1])

    #sorts the keys by number and then alphabetical
    keysort = sorted(names.keys(), key = lambda a: (-names[a], a))

    #prints the answer out
    print (len(keysort))
    for k in keysort:
        print (k, names[k])
