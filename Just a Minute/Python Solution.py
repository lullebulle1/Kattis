#stores total minutes and total seconds
totM, totS = 0, 0

#for each observation
for i in range(0,int(input())):
    #scan in input
    minutes, seconds = list(map(int,input().split(' ')))
    
    #adds input to above variables
    totM+=minutes
    totS+=seconds

#prints out the solution with rounding to 9 decimals
print(round(totS/(60*totM),9) if totS/(60*totM)>1 else "measurement error")
