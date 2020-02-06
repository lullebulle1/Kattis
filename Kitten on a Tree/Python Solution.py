#the recursive function to find the path
def findLower(x):
    #for each unique element in the passed input
    for i in x:
        #finds other possible matches that contain that number
        possNumbs = [y for y in fullList if i in y and y!= x]

        #if the length is 0, we have found out end, so return that #
        if(len(possNumbs)==0):
            return i

        #otherwise loop through each possible match
        for j in possNumbs:
            #redoes loop with that possible array
            temp = findLower(j)

            #if match was found, return the string of numbers
            if(temp!=0):
                return "{} {}".format(str(i),str(temp))


#the entire list of possibilities
fullList = [[int(input())]]
inp = list(map(int, input().split(' ')))

#takes in the input and assigns it to the list
while(inp[0]!="-1"):
    fullList.append(list(map(int, inp)))
    inp = list(input().split(' '))

#prints the output
print(findLower(fullList[0]))
