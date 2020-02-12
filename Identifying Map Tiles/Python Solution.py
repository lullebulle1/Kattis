#takes in inputs
i = list(input())

#variables
left, top = 0, 0
level = 0

#loops through and adds tiles to left and top
for y in i:
    x = int(y)
    left = left*2 + x%2
    top = top*2 + (1 if x==2 or x==3 else 0)
    level += 1

#prints the output
print(level,left,top)
