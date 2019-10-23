secret = list(input())
letters = ['P','E','R']
count=0;

for i in range (0,len(secret)):
    if(secret[i]!=letters[i%3]):
        count+=1;
print(count)
