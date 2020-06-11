import string

#create a list of all elements
x = list(string.ascii_lowercase)
x.insert(0, " ")

#for each test case
for i in range(int(input())):
    tmp = list(input())
    key = tmp.pop(0)
    mssg = tmp [1:]

    #runs ecryption scheme
    if (key=="e"):
        count = 0
        out = ""
        for j in mssg:
            out += x[(count + x.index(j))%27]
            count += x.index(j)
        print (out)  

    #finds appropriate letters in decryption scheme
    else:
        count = 0
        out = ""
        for j in mssg:
            tmp = x.index(j)
            for k in range(27):
                if ((k+count)%27 == tmp):
                    count += k
                    out += x[k]
                    break
        print (out)
