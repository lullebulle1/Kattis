from math import sqrt, floor
def fib(n):
    #note: doing this recursively times out as input increase
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

times = int(input())
print(floor(fib(times-1)),floor(fib(times)))
