#takes in all input
x = int (input())
arr = list(map(int, input().split()))

#calculates arr of numbers with exactly 1 role. Prints answer
out = [i for i in range (1,7) if arr.count(i)==1]
if (len(out) == 0):
    print ("none")
else:
    print (arr.index(max(out))+1)
