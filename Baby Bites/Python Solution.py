#takes in the input
count = int(input())
words = list(input().split(' '))

#goes through the iterations and if the number matches, it's fine
for i in range(1, count+1):
    if(words[i-1]!='mumble' and int(words[i-1])!=i):
        print("something is fishy")
        exit()

#if it completed the loop, his count is fine
print("makes sense")
