#scans in the numbers
e, f, c = list(map(int,input().split(' ')))

bottles = e+f
drank = 0

#whiles he can trade in bottles, he drinks another, adding another bottle
while (bottles>=c):
    bottles=bottles+1-c
    drank+=1

#prints the amount that he drank
print(drank)

