numbers = input().split(' ')
a = int("".join(list(numbers[0])[::-1]))
b = int("".join(list(numbers[1])[::-1]))
print(a if a>b else b)
