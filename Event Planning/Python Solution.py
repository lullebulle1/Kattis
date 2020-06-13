n, b, h, w = list(map(int, input().split()))
minprice = b+1

for i in range(h):
    price = int(input())
    beds = list(map(int, input().split()))

    #calculates lowest possible price for hotels with enough seating 
    maxbeds = [x for x in beds if x>=n]
    if (len(maxbeds) > 0):
        if (n*price<minprice):
            minprice = n*price

print (minprice if minprice <= b else "stay home")
