import sys
from math import floor
 
for line in sys.stdin:
    M, P, L, E, R, S, N = list(map(int, line.split()))

    newM, newP, newL = 0, 0, 0
    for i in range(N):
        newL = M * E
        newP = floor(L/R)
        newM = floor(P/S)
        L, P, M = newL, newP, newM
    print(M)
