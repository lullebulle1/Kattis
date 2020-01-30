#defines a lambda that will return the name of the person if they ate the passed food
def inArr(arr, name):
    return lambda a: name if a in arr else "" 

#takes in the number iterations input
x = int(input())

#goes while it hasn't scanned in a 0
while(x!=0):
    #defines the list of food and people, respectively
    myList = []
    people = []

    #for each line we have
    for i in range(x):
        #takes input and then adds all new food to myList, and creates a lambda
        #for each person and adds to people list
        arr = list(input().split(' '))
        myList = list(set().union(myList,arr[1::]))
        people.append(inArr(arr[1::], arr[0]))

    #sorts the food array
    myList.sort()

    #for each food item
    for i in range(len(myList)):
        #gets results of the lambda functions and sorts it
        result = [x(myList[i]) for x in people if x(myList[i])!="" ]
        result.sort()

        #prints the answer
        print(myList[i], ' '.join(result))
    
    #prints a new line
    print()

    #takes in input for next case
    x = int (input())
