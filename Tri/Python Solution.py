#Note: Using eval is dangerous because it can run pretty much anything
numbs = list(map(int,input().split(' ')))
ops = ["+","-","/","*"]

for i in range(4):
    evalString = "{}{}{}".format(numbs[0],ops[i],numbs[1])
    evalString2 = "{}{}{}".format(numbs[1],ops[i],numbs[2])
    
    if eval(evalString+"=={}".format(numbs[2])):
        print(evalString+"={}".format(numbs[2]))
        break
    elif eval("{}==".format(numbs[0])+evalString2):
        print("{}=".format(numbs[0])+evalString2)
        break

