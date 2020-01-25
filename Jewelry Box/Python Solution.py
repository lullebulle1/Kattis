#needs for sqrt a function
from math import sqrt

#for each test cast given
for i in range(0,int(input())):
    #splits the inputs into either x or y
    x, y = list(map(int,input().split(' ')))

    #by maximizing the volume using calculus, you get this
    #Need the quadratic formula, so two possible cases for maximum height
    posH1 = (4*(x+y)+sqrt((4*(x+y))**2-48*x*y))/24
    posH2 = (4*(x+y)-sqrt((4*(x+y))**2-48*x*y))/24

    #solves the two possible volumes given the different heights found above
    sol1 = (y-2*posH1)*(x-2*posH1)*posH1    
    sol2 = (y-2*posH2)*(x-2*posH2)*posH2 

    #prints the greater of the two volumes
    print(round(max(sol1, sol2),11))
