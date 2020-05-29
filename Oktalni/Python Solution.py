x = input()
while (len(x)%3 != 0):
    x = "0"+x

out = ""
for i in range(0, len(x), 3):
    out += str(int (x[i:i+3], 2))

print (out)
