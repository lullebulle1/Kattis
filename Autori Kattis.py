inputs = input().split('-')
outputs = ""

for i in range (0,len(inputs)):
    outputs+=list(inputs[i])[0]
print(outputs)
