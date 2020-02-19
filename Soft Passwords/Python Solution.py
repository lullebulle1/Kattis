#takes in input and finds strings with numbers pre/appended
S = input()
P = input()
P2 = [str(i)+P for i in range(10)]
P3 = [P+str(i) for i in range(10)]

#goes through each scenario
if (S==P):
    print("Yes")
elif (S in P2):
    print("Yes")
elif (S in P3):
    print("Yes")
elif (S.swapcase()==P):
    print("Yes")
else:
    print("No")
