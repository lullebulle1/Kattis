x = []
found = 0

#takes in all the input and adds it to x
for i in range(int(input())):
    x.append(int(input()))

#goes through all # between 1 and highest
for j in range(1,x[len(x)-1]):
    if(j not in x):
        found=1
        print(j)

#if none found print good job
if(found==0):
    print("good job")
