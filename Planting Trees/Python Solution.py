numb = int(input())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

minday = 0
for i in range(numb):
    if (minday < trees[i]+i+1):
        minday = trees[i]+i+1

print(minday+1)
