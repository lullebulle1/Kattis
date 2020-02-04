#imporst uppercase letters and system
import sys
from string import ascii_uppercase

#for each line in the input
for line in sys.stdin:
    #take the input and split it
    a = line.split(' ')

    #takes input and assigns to name or number array depending on type
    name = [x for x in a if x[0] in ascii_uppercase]
    numbs = [float(x) for x in a if x[0] not in ascii_uppercase]

    #prints the result
    print(round(sum(numbs)/len(numbs),6), ' '.join(name))
