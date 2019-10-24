values = list(map(int,input().split(' ')))
X = values[0]
Y = values[1]

for i in range (1,values[2]+1):
    divx = i%X == 0
    divy = i%Y == 0

    if( divx and divy):
        print("FizzBuzz")
    elif (divx):
        print("Fizz")
    elif (divy):
        print("Buzz")
    else:
        print(i)
