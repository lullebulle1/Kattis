#takes in the input
a, b, c, n = list(map(int,input().split(' ')))

#pints the answer
print("YES" if a!=0 and b!=0 and c!=0 and n>=3 and a+b+c>=n else "NO")
