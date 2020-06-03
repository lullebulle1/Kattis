numb = int(input())
arr = list(map(int, input().split()))
out = [str(arr[0])]

for i in range(len(arr)):
    if (arr[i] > int(out[-1])):
        out.append(str(arr[i]))

print (len(out))
print (' '.join(out))
