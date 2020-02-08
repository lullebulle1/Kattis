#inputs
p, q, s = list(map(int, input().split(' ')))

#goes through all numbers and if modulo of both are in it
#prints yes
for i in range (1,s+1):
    if(i%p==0 and i%q==0):
        print("yes")
        exit()

#if it gets here, it prints no
print("no")
