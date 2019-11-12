numbs = list(map(int,input().split(' ')))
dif = numbs[1]-numbs[0]

if(dif>1):
    print("Dr. Chaz will have {} pieces of chicken left over!".format(dif))
elif dif == 1 or dif == 0:
    print("Dr. Chaz will have {} piece of chicken left over!".format(dif))
elif dif == -1:
    print("Dr. Chaz needs {} more piece of chicken!".format(abs(dif)))
else:
    print("Dr. Chaz needs {} more pieces of chicken!".format(abs(dif)))
