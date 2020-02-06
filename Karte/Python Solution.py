#takes in input
inp = input()

#separate arrays for each card suit
P = []
K = []
H = []
T = []

#error check
err = 0

#for each substring of cards add to array and err if already in it
for i in range(0,len(inp),3):
    sub = inp[i+1:i+3]
    if(inp[i]=="P"):
        if (sub in P):
            err=1    
        P.append(sub)
    if(inp[i]=="K"):
        if (sub in K):
            err=1    
        K.append(sub)
    if(inp[i]=="H"):
        if (sub in H):
            err=1    
        H.append(sub)
    if(inp[i]=="T"):
        if (sub in T):
            err=1    
        T.append(sub)

#prints results
if(err):
    print("GRESKA")
else:
    print(13-len(P),13-len(K),13-len(H),13-len(T))
