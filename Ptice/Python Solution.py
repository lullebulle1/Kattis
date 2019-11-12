from math import ceil

numbQ = int(input())
answers = list(input())
Adrian = list("ABC"*ceil(numbQ/3))
Bruno = list("BABC"*ceil(numbQ/4))
Goran = list("CCAABB"*ceil(numbQ/6))
a,b,c = 0,0,0

for i in range(numbQ):
    if(Adrian[i]==answers[i]):
        a+=1
    if(Bruno[i]==answers[i]):
        b+=1
    if(Goran[i]==answers[i]):
        c+=1

res = max(a,b,c)
print(res)
print("Adrian\n" if a==res else "",end="")
print("Bruno\n" if b==res else "",end="")
print("Goran" if c==res else "")
