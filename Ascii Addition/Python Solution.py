#all of the words arts
zero = "xxxxx"+"x...x"*5+"xxxxx"
one = "....x"*7
two = "xxxxx"+"....x"*2+"xxxxx"+"x...."*2+"xxxxx"
three = "xxxxx"+"....x"*2+"xxxxx"+"....x"*2+"xxxxx"
four = "x...x"*3+"xxxxx"+"....x"*3
five = "xxxxx"+"x...."*2+"xxxxx"+"....x"*2+"xxxxx"
six = "xxxxx"+"x...."*2+"xxxxx"+"x...x"*2+"xxxxx"
seven = "xxxxx"+"....x"*6
eight = "xxxxx"+"x...x"*2+"xxxxx"+"x...x"*2+"xxxxx"
nine = "xxxxx"+"x...x"*2+"xxxxx"+"....x"*2+"xxxxx"
numbarr = [zero, one, two, three, four, five, six, seven, eight, nine]

#returns the number of the ascii art
def retNumb (string):
    for i in range(10):
        if (string == numbarr[i]):
            return i
    return -1

#takes in input
arts = []
for i in range(7):
    arts.append(input())

#appends to two different variables
a = ""
b = ""
plus = False
for j in range(0, len(arts[0]), 6):
    string = ''.join([arts[x][j:j+5] for x in range(7)])
    numb = retNumb(string)
    if (numb == -1):
        plus = True
        continue

    if (plus):
        b += str(numb)
    else:
        a += str(numb)

#calculates the output
out = str(int(a)+int(b))
outarr = []
for k in range(7):
    tmp = []
    for l in out:
        tmp.append(numbarr[int(l)][5*k:5*(k+1)])
    outarr.append('.'.join(tmp))
print ('\n'.join(outarr))
