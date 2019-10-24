letters = list(input())
G, T, C = letters.count("G"), letters.count("T"), letters.count("C")
total = min([G,T,C])*7 + G**2 + T**2 + C**2

print(total)
