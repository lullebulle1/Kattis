x = int(input())
prev = input()
curr = ""
count = 0

for i in range(x-1):
    curr = input()
    if (prev == curr):
        count += 1
    prev = curr
print (count)
