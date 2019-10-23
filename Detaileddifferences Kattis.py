for i in range (0, int(input())):
    a = list(input())
    b = list(input())
    output = ""
    for j in range (0, len(a)):
        output += "*" if a[j]!=b[j] else "."
    print("".join(a)+"\n"+"".join(b)+"\n"+output+"\n\n")
     
