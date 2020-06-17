n1, n2 = input(), input()
l1, l2 = len(n1), len(n2)

#pads each number with 0' up front
minlen = min (l1, l2)
n1, n2 = "0"*(l2-minlen) + n1, "0"*(l1-minlen) + n2

#adds to output each comparison
out1, out2 = "", ""
for i in range(max(l1,l2)):
    if (int(n1[i]) > int(n2[i])):
        out1 += n1[i]
    elif (int(n1[i]) < int(n2[i])):
        out2 += n2[i]
    else:
        out1 += n1[i]
        out2 += n2[i]

#prints answer
print ("YODA" if len(out1)==0 else int(out1))
print ("YODA" if len(out2)==0 else int(out2))
