#number of balloons and the bottle array
numbBalloons = int(input())
bottles = list(map(int,input().split(' ')))

#sorts bottles and calculates ratio of fill for each balloon
bottles.sort()
balloons = [bottles[x]/(x+1) for x in range(numbBalloons)]

#prints the lowest ration as long as the highest isn't above 1
print(min(balloons) if max(balloons)<=1 else "impossible")
