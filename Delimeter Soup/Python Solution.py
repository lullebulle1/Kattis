x = int(input())
inp = list(input())

start = []
count = 0
for i in inp: 
    if (i == "(" or i=="{" or i=="["):
        start.append(i)
    elif (i != " "):
        if (len(start) == 0):
            print ("{0} {1}".format(i, count))
            exit()
        tmp = start.pop(-1)
        if ((tmp == "{" and i != "}") or (tmp == "(" and i != ")") or (tmp == "[" and i != "]")):
            print ("{0} {1}".format(i, count))
            exit()
    count += 1

print ("ok so far")
