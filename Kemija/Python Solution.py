inputs = input()
vowels = ['a','e','i','o','u']
out = ''
i = 0

while i<len(inputs):
    out=out+inputs[i]
    i += 3 if inputs[i] in vowels else 1
    
print(out)
