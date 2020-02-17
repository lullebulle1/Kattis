#goes until it finds a 0, count is the iteration it's on
count = 1
while True:
    x = int(input())
    if(x==0):
        break
    
    #create a dictionary and adds unique animals to it
    dic = {}
    for j in range(x):
        animal = list(input().split(' '))
        species = animal[len(animal)-1].lower()
    
        if(species in dic.keys()):
            dic[species] += 1
        else:
            dic[species] = 1

    #finds all the keys of the dict and prints them out after sorting the keys
    print("List {}:".format(count))
    keys = [x for x in dic.keys()]
    keys.sort()
    for i in keys:
        print("{} | {}".format(i,dic[i]))
    count+=1
