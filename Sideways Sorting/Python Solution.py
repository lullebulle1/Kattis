#rotates the array so can sort by column and then back to normal
def rot (arr, c, r):
    outarr = []
    for i in range(c):
        tmp = []
        for j in range(r):
            tmp.append(arr[j][i])
        outarr.append(''.join(tmp))
    return outarr

x = input()
while (x[0] != "0"):
    r, c = list(map(int, x.split()))
    arr = []
    for i in range (r):
        arr.append(list(input()))
    
    #rotates array and sorts using above function
    arr2 = rot(arr, c, r)
    arr2 = sorted(arr2, key=str.lower)
    print ('\n'.join(rot(arr2, r, c)))
    print ()
    x = input()
