board = []
out = 1

def consect (s):
    for k in range(len(s)-2):
        substr = s[k:k+3]
        if(substr.count("W")>=3 or substr.count("B")>=3):
            return True
    return False

for i in range(int(input())):
    board.append(list(input()))

for j in range(len(board)):
    row = board[j]
    col = [x[j] for x in board]

    if(row.count("W")!=row.count("B") or col.count("W")!=col.count("B")):
        out=0
        break
    elif(consect(row) or consect(col)):
        out=0
        break

print(out)
