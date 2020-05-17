from statistics import mean

x = int(input())
score = 0
score2 = 0

data = []
for i in range(x):
    data.append(int(input()))

for i in range(x):
    score += data[i]*(4/5)**(i)

count = 0
avg = []
for i in range(x):
    for j in range(x):
        if (j!=i):
            score2 += data[j]*(4/5)**(count)
            count+=1
    avg.append((1/5)*score2)
    count = 0
    score2 = 0

print (score/5)
print (mean(avg))
