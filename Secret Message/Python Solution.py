import math

numb = int(input())
for i in range(numb):
    x = input()
    lens = len(x)
    square = math.ceil(lens**(1/2))
    x += "*"*(square**2-lens)

    arr = []
    for i in range(square):
        arr.append(x[i*square:(i+1)*square])

    output = ""
    for row in range(square):
        for col in range(square-1,-1,-1):
            output += arr[col][row]

    output = [y for y in output if y!="*"]
    print(''.join(output))
