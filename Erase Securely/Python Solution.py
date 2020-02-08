#takes in input and calculates if multiple of 2
reps = int(input())
repsStat = reps%2

#takes in the two strings
before = list(input())
after = list(input())

#constructs what the list should become and prints if it did become that
out = [x if repsStat==0 else str((int(x)+1)%2) for x in before]
print("Deletion succeeded" if after==out else "Deletion failed")
