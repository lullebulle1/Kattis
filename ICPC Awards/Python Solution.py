x, teams = 0, int(input())
winners = []

while x<12:
    inputs = input().split(' ')

    if(inputs[0] not in winners):
        winners.append(inputs[0])
        print(' '.join(inputs))
        x+=1
    
