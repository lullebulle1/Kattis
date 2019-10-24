for i in range(int(input())):
    places = []
    for j in range(int(input())):
        x = input()
        if (x not in places):
            places.append(x)
    print(len(places))
