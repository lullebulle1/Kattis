first = int(input())
sec = int(input())

dif = abs(first-sec)
otherdif = 360-dif

if (dif == otherdif):
    print(180)
elif (first > sec):
    if (dif > otherdif):
        print (otherdif)
    else:
        print (-1*dif)
else:
    if (dif > otherdif):
        print (-1*otherdif)
    else:
        print (dif)
