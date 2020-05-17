s, t, n = list(map(int, input().split()))
d = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

time = s

for i in range(n):
    time += d[i]
    time += abs(time-c[i]) % c[i]
    time += b[i]

time+=d[n-1]
print ("yes" if time<=t else "no")
