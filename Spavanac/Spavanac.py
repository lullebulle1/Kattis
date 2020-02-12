#takes in input
hours, minutes = list(map(int,input().split(' ')))

#subtracts minutes
minutes-=45

#changes around hours and minutes to match new time
hours = hours-1 if minutes<0 else hours
hours = 23 if hours<0 else hours
minutes = minutes+60 if minutes<0 else minutes

#prints new time
print(hours, minutes)
