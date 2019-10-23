total = 0;
for i in range(0, int(input())):
    x = [char for char in input()]    
    y = ''.join(x[0:-1])
    power = int(x.pop(-1))
    total+=int(y)**power

print(total)
    
    
