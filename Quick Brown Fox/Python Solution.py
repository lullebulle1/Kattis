#needed for ascii_lowercase string
import string

#for each case
for i in range(0,int(input())):
    #take in the input and only put letters to the output if it isn't in input
    x = input().lower()
    output = [y for y in string.ascii_lowercase if y not in x]
   
    #prints the result 'pangram' if all letters used otherwise the missing letters
    print("pangram" if len(output)==0 else "missing {}".format(''.join(output)))

