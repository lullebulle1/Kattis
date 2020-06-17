from itertools import permutations as per

#takes in the input
x = list(map(int, input().split()))
h2, h1 = x.pop(-1), x.pop(-1)

#not necessarily the quickest way, but still fast
#loops each permuation and calculates sum to compare to heights
for y in per(x):
    s1, s2 = sum(y[0:3]), sum(y[3:])
    if (s1 == h1 and s2 == h2):
        t1 = ' '.join(list(map(str, sorted(y[0:3], reverse=True))))  
        t2 = ' '.join(list(map(str, sorted(y[3:], reverse=True))))  
        print ("{} {}".format(t1, t2))
        break
