#calculates amount of months since start of 2018
months = 12 * (int(input()) - 2018)

#sees if the date fall within the year
for i in range(12):
    if ((months+i)%26 == 3):
        print ("yes")
        exit()
print("no")
