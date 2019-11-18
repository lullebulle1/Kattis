#1, 3, 5, ... => either
#2, 6, 10, ... => odd
#4, 8, 12, ... => even

x = int(input())
if(x%2 == 1):
    print("Either")
elif(x%4 == 2):
    print("Odd")
else:
    print("Even")
