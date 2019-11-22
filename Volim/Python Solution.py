player = int(input())-1
time = 0
for i in range(int(input())):
    t_quest, response = input().split(' ')

    time+=int(t_quest)
    if(time>=210):
        print(player%8+1)
        break

    if (response=="T"):
        player+=1
