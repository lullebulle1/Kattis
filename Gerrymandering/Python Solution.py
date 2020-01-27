#imports the floor function
from math import floor

#takes in the number of precincts and districts
prec, dist = list(map(int,input().split(' ')))

#creates arrays for storing data and results of size dist
data = [[0,0] for i in range(dist)]
results = [0 for i in range(dist+1)]

#takes in all the data and assigns it into data array
for i in range(0,prec):
    distNumb, votesA, votesB = list(map(int,input().split(' ')))
    data[distNumb-1][0] += votesA
    data[distNumb-1][1] += votesB

#goes through each data set and does the calculation
for i in range(0, dist):
    a = data[i][0]
    b = data[i][1]

    winner = "A" if a>b else "B"

    #calculates wasted votes for both parties
    wastedA = a - floor((a+b)/2)-1
    wastedB = b - floor((a+b)/2)-1    
    wastedA = wastedA if wastedA>=0 else a
    wastedB = wastedB if wastedB>=0 else b

    #stores results to be used to calculate efficiency
    results[i] = wastedA - wastedB
    results[dist] += a+b

    #prints results for each district
    print(winner, wastedA, wastedB)

#prints out the efficiency
print(round(abs(sum(results[0:dist])/results[dist]),10))

