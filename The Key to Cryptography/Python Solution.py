cipher = input()
key = input()
output = ""

lens = len(key)
for i in range(len(cipher)):
    if (i < lens):
        output += chr(65 + (ord(cipher[i]) - ord(key[i]))%26)
    else:
        output += chr(65 + (ord(cipher[i]) - ord(output[i-lens]))%26)

print(output)
