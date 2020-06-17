for i in range(int(input())):
    #takes in all words
    words = list(input().split())
    
    #loops through each sounds for each animal
    x = list(input().split())
    while (x[0] != "what"):
        words = [y for y in words if y!=x[2]]
        x = list(input().split())

    #prints it
    print (' '.join(words))
