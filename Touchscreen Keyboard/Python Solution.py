keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

#calculates the distances between letters in the word
def worddist (word, altword):
    row, col = 0, 0
    rowa, cola = 0, 0
    sums = 0

    for l in range(len(word)):
        k = word[l]
        if (k in keyboard[0]):
            row = 0
            col = keyboard[0].find(k)
        elif (k in keyboard[1]):
            row = 1
            col = keyboard[1].find(k)
        elif (k in keyboard[2]):
            row = 2
            col = keyboard[2].find(k)

        k = altword[l]
        if (k in keyboard[0]):
            rowa = 0
            cola = keyboard[0].find(k)
        elif (k in keyboard[1]):
            rowa = 1
            cola = keyboard[1].find(k)
        elif (k in keyboard[2]):
            rowa = 2
            cola = keyboard[2].find(k)
        sums += abs(row-rowa) + abs(col-cola)

    return sums


for i in range(int(input())):
    word, amount = list(input().split())
    alts = []

    #adds to list and sorts with a lambda function by dist then alpha
    for j in range(int(amount)):
        alts.append(input())
    alts.sort(key=lambda x: (worddist(word, x), x))

    for j in alts:
        print ("{} {}".format(j, worddist(word, j)))
