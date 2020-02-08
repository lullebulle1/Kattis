#takes in the input
numbs = int(input())
arr = list(map(int, input().split(' ')))

#sorts the array
arr.sort(reverse=True)

#counts all elements for each person based on position
alice = sum([x for i, x in enumerate(arr) if i%2==0])
bob = sum([x for i, x in enumerate(arr) if i%2==1])

#prints the integers
print(alice, bob)
