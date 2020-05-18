message = input()
key = input()

count = 0
for i in message:
    msschr  = ord(i)%65
    keychr = ord(key[count])%65
    newmsg = 65

    if (count%2 == 1):
        newmsg += (msschr+keychr)%26
    else:
        newmsg += (msschr-keychr)%26

    count+=1
    print(chr(newmsg), end='')

print()
