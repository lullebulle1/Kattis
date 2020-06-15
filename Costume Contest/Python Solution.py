from collections import Counter

#takes input, sorts by count and then alphabetical, then prints
counter = Counter([input() for x in range(int(input()))])
mins = min([counter[a] for a in counter])
arrsort = sorted([x for x in counter if counter[x]==mins], key=lambda a: (counter[a], a))
print (' '.join(arrsort))
