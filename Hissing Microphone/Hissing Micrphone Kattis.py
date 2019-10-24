x = list(input())
for i in range(0, len(x)-1):
    if (x[i]==x[i+1] and x[i]=="s"):
        print("hiss")
        quit()
print("no hiss")
