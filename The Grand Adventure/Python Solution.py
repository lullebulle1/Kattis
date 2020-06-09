for i in range(int(input())):
    x = [k for k in input() if k!="."]
    prev = []
    for j in x:
        if (j == "*" or j == "$" or j == "|"):
            prev.append(j)
        elif (j == "t"):
            if (len(prev)>0 and prev[-1] == "|"):
                prev.pop(-1)
            else:
                prev.append("tmp")
                break
        elif (j == "b"):
            if (len(prev)>0 and prev[-1] == "$"):
                prev.pop(-1)
            else:
                prev.append("tmp")
                break
        elif (j == "j"):
            if (len(prev)>0 and prev[-1] == "*"):
                prev.pop(-1)
            else:
                prev.append("tmp")
                break
    if (len(prev)>0):
        print ("NO")
    else:
        print ("YES")
