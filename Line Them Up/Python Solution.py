names = []
for i in range(int(input())):
    names.append(input())

adjust = [x for x in names]
adjust.sort()

if(names == adjust):
    print("INCREASING")
elif(names==adjust[::-1]):
    print("DECREASING")
else:
    print("NEITHER")
