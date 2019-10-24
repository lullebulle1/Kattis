array = list(input().split(' '))
suit = array[1]
total = 0

for i in range(0, int(array[0])*4):
    hand = list(input())
    
    if (hand[0] == "A"):
        total+=11
    elif (hand[0] == "K"):
        total+=4
    elif (hand[0] == "Q"):
        total+=3
    elif (hand[0] == "J"):
        total+=2
        if(hand[1]==suit):
            total+=18
    elif (hand[0]=="T"):
        total+=10
    elif (hand[0]=="9" and hand[1]==suit):
        total+=14

print(total)
        
