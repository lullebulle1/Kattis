#takes in input
numb, time = list(map(int,input().split(' ')))
probs = list(map(int,input().split(' ')))

#variables
count = 0
i = 0

#loops through
while(i<numb and count+probs[i]<=time):
    count += probs[i]
    i+=1

#prints answer
print(i)
