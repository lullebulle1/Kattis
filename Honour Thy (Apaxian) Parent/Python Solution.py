fname, lname = input().split(' ')
vowels = list("aiou")
x = len(fname)

if(fname[x-2::] == "ex"):
    print("{}{}".format(fname,lname))
elif(fname[x-1::] == "e"):
    print("{}x{}".format(fname,lname))
elif(fname[x-1::] in vowels):
    print("{}ex{}".format(fname[0:x-1],lname))
else:
    print("{}ex{}".format(fname,lname))
