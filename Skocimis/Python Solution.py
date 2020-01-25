#takes in input
a, b, c = list(map(int, input().split(' ')))
count=0

#decides if the gap between the first two element is greater than the the second
#switches element c to be a+1
if(b-a>=c-b and a+2!=c):
    b, c = a+1 , b
    count+=1

#keeps going until the elements are all in line
while(a+2!=c):
    a, b = b, b+1
    count+=1

#prints solution
print(count)
