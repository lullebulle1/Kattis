for i in range(int(input())):
    numbs = list(map(int,input().split(' ')))
    power, out = 1, 0
    
    while True:
        #this finds the maximum possible power that the base can be take to
        if (numbs[1]**power < numbs[2]):
            power+=1
            continue
        break
    
    for x in range(power,0,-1):
        #this function walks backwards from maxpower to 0
        heighest = 0.0
        while True:
            if (numbs[2]/(numbs[1]**x*(heighest+1))>=1):
                heighest+=1
                continue
            #it will add the square of the maximum integer that works with this power
            out += heighest**2
            #subtracts from the original value so smaller powers work
            numbs[2]=numbs[2]-(numbs[1]**x)*heighest
            break
    print(i+1, int(out+numbs[2]**2))
