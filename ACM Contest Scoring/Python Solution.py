time, correct = 0, 0
x = input().split(' ')
prev = []

while(int(x[0]) != -1):
    if(x[2]=="right"):
        correct+=1
        time+=int(x[0])
        for y in prev:
            if (y[1]==x[1]):
                time+=20

    prev.append(x)
    x = input().split(' ')

print(correct, time)
