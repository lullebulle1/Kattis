arr = list(input().split(' '))
print("no" if len([x for x in arr if arr.count(x)>1]) else "yes")
