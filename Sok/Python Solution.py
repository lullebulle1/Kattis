#takes in input and calculates the lowest ration
x = list(map(int, input().split(" ")))
y = list(map(int, input().split(' ')))
ratios = [x[i]/y[i] for i in range(len(x))]
lowRat = min(ratios)

#prints out the left overs
for i in range(len(x)):
    print(round(x[i]-(y[i]*lowRat),6),end=' ')
