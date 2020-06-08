h, w, n = list(map(int, input().split()))
brick = list(map(int, input().split()))

layer = 0
width = 0
for i in brick:
    if (layer == h):
        break
    if (width + i > w):
        print ("NO")
        exit()
    elif (width + i == w):
        layer += 1
        width = 0
    else: 
        width += i
print ("YES")
