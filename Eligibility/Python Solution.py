#for each condition
for i in range(0, int(input())):
    #takes in the input
    name, begin, dob, courses = list(input().split(' '))
    
    #goes through the eligibility conditions and prints the correct answer
    if(int(begin.split('/')[0])>=2010 or int(dob.split('/')[0])>=1991):
        print(name, "eligible")
    elif(int(courses)>40):
        print(name, "ineligible")
    else:
        print(name, "coach petitions")
        
    
