total = 0
inputs = [input(),input(),input(),input(),input()]
response=""

if(len([x for x, y in enumerate(inputs) if "FBI" in y])):
    for i in range (0,5):
        if("FBI" in inputs[i]):
            response+=str(i+1)+" "

    print(response)
else:
    print("HE GOT AWAY!")

