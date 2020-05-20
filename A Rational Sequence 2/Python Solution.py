def solve(l, r):
    if (l == r):
        return 1

    if(l > r):
        return 2*solve(l-r,r) + 1

    if (l < r):
        return 2*solve(l, r-l) 

for i in range(int(input())):
    numb, string = list(input().split(' '))
    a, b = list(map(int, string.split('/')))
    print(numb, solve(a,b)) 
