#goes until the input is 0 0
while True:
    #takes in input
    x, y = list(map(int, input().split(' ')))
    
    #ends the loop if 0 0 
    if(x==0 and y==0):
        break

    #goes through the different conditions possible
    if(x+y == 13):
        print("Never speak again.")
    elif(x>y):
        print("To the convention.")
    elif(x<y):
        print("Left beehind.")
    else:
        print("Undecided.")
