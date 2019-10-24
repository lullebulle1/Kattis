array = list(map(int,input().split(' ')))
correct = [1,1,2,2,2,8]
answer = ""

for i in range (0,6):
    answer+=str(correct[i]-array[i])+" "

print(answer)
