one = "  *"*5
two = "***  *****  ***" 
three = "***  ****  ****"
four = "* ** ****  *  *"
five = "****  ***  ****"
six = "****  **** ****"
seven = "***  *  *  *  *"
eight = "**** ***** ****"
nine = "**** ****  ****"
zero = "**** ** ** ****"

inp1, inp2, inp3, inp4, inp5 = input(), input(), input(), input(), input()

def findnumb(x):
    if (x == one):
        return 1
    elif (x == two):
        return 2
    elif (x == three):
        return 3
    elif (x == four):
        return 4
    elif (x == five):
        return 5
    elif (x == six):
        return 6
    elif (x == seven):
        return 7
    elif (x == eight):
        return 8
    elif (x == nine):
        return 9
    elif (x == zero):
        return 0
    return -1

outnumb = ""
for i in range (0, len(inp1), 4):
    numb = inp1[i:i+3] + inp2[i:i+3] + inp3[i:i+3] + inp4[i:i+3] + inp5[i:i+3]
    numbreturn = findnumb(numb) 

    if (numbreturn == -1):
        print ("BOOM!!")
        exit()
    else:
        outnumb += str(numbreturn)

outnumb = int(outnumb)
print ("BEER!!" if outnumb%6==0 else "BOOM!!")
