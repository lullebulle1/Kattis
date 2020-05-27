from itertools import permutations 

inp = int(input())
l = list(permutations(list(str(inp)))) 
l.sort()

for i in l:
    if (int(''.join(i)) > inp):
        print(int(''.join(i)))
        exit()

print (0)
