#takes in input
rooms, booked = list(map(int, input().split(' ')))

#if no rooms available
if(rooms==booked):
    print("too late")
    exit()

#gets the input
roomArr = []
for i in range(booked):
    roomArr.append(int(input()))

#loops through to find the first available room
for i in range(1, rooms+1):
    if (i not in roomArr):
        print(i)
        break
