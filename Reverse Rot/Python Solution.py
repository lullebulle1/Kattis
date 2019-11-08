chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")

while True:
    inputs = input().split(' ')
    if(inputs[0]=="0"):
        break
    
    revString= inputs[1][::-1]
    output=""

    for i in range(len(revString)):
        output+=chars[(chars.index(revString[i])+int(inputs[0]))%28]
            
    print(output)    
