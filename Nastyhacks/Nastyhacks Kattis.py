for i in range (0,int(input())):
    array = list(map(int, input().split(' ')))

    if(array[1]-array[2]>array[0]):
        print("advertise")
    elif (array[1]-array[2]==array[0]):
        print("does not matter")
    else:
        print("do not advertise")

