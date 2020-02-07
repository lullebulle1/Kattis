#input
start, end = list(map(int,input().split(' ')))

#goes through the range specified, and counts possible combos
count = 0
for i in range(start,end+1):
    #if 0 is part of the string, not possible ever
    if('0' in str(i)):
        continue

    failure = 0
    
    #checks to see if all numbers are special
    for j in str(i):
        if str(i).count(j)>1:
            failure=1
            break

    #exits if they werent
    if(failure==1):
        continue

    #checks to see if all numbers divide i
    for j in str(i):
        if (i%int(j)!=0):
            failure=1
            break

    #eixts it they didnt
    if(failure==1):
        continue
    
    #adds to count if passed all above criteria
    count+=1

#prints the answer
print(count)
