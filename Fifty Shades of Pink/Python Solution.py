x = int(input())
count = 0

for i in range(x):
    y = input().lower()
    count += 1 if "pink" in y else 1 if "rose" in y else 0

print(count if count>0 else "I must watch Star Wars with my daughter")
