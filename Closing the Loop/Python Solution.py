for i in range(1,int(input())+1):
    numb = int(input())
    ropes = list(input().split(' '))
    length = 0

    #takes the ropes input and splits the lengths of each into either
    #the b array or the r array, strips it of the letter
    b = [int(x[:-1]) for x in ropes if "B" in x]
    r = [int(x[:-1]) for x in ropes if "R" in x]

    #sorts the arrays
    b.sort(reverse=True)
    r.sort(reverse=True)

    #goes through, to the max of the shortest array to find the length
    for j in range(min(len(b),len(r))):
        length += b[j] + r[j] - 2

    print("Case #{}: {}".format(i,length))
