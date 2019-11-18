for i in range(int(input())):
    numb, days = input().split(' ')
    print(numb, int(.5*int(days)**2 + 1.5*int(days)))
