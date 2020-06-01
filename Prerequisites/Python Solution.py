inps = list(map(int, input().split()))

while (inps[0] != 0):
    courses = list(input().split())
    possible = True

    #goes for each row of courses 
    for i in range(inps[1]):
        #takes in the line
        cats = list(input().split())

        #finds all matches of courses and compares to reqs
        catcourses = [x for x in cats[2:] if x in courses]
        if (len(catcourses) < int(cats[1])):
            possible = False

    #prints the answer and takes new input
    print ("yes" if possible else "no")
    inps = list(map(int, input().split()))
