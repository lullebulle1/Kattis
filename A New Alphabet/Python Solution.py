import string

newalpha = ['@','8','(','|)','3','#','6','[-]','|','_|','|<','1','[]\/[]','[]\[]','0','|D','(,)','|Z','$',"']['",'|_|','\/','\/\/','}{',"`/",'2']

x = input()
for i in x.lower():
    if (i in string.ascii_lowercase):
        print (newalpha[ord(i)-97], end='')
    else:
        print(i, end='')

print()
