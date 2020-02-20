#program loops through input and checks conditions
people = []
for i in range(int(input())):
    inp = list(input().split(' '))

    if(inp[0]=="entry"):
        if(inp[1] not in people):
            people.append(inp[1])
            print("{} entered".format(inp[1]))
        else:
            print("{} entered (ANOMALY)".format(inp[1]))
    else:
        if(inp[1] not in people):
            print("{} exited (ANOMALY)".format(inp[1]))
        else:
            people.remove(inp[1])
            print("{} exited".format(inp[1]))
