numb = int(input())
print(sum([abs(int(x)) for x in list(input().split(' ')) if int(x)<0]) if numb!=0 else "0")
