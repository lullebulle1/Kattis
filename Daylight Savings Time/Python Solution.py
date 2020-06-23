import datetime

#for each input
for i in range (int(input())):
    #takes in input and creates timedelta objects of them
    direct, D, H, M = list(input().split())
    origtime = datetime.timedelta(hours = int(H), minutes = int(M))
    diftime = datetime.timedelta(minutes = int(D))
    outstr = ""

    #does the calculations
    if (direct == "F"):
        outstr = str(origtime + diftime)
    else:
        outstr = str(origtime - diftime)

    #strips anything that says day
    if ("," in outstr):
        outstr = outstr[outstr.index(",")+2:]

    #prints the hours and minute
    out = list(outstr.split(":"))
    print (int(out[0]), int(out[1]))
