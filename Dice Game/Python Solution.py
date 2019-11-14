Gunnar = sum(list(map(int,input().split(' '))))
Emma = sum(list(map(int,input().split(' '))))

print("Gunnar" if Gunnar>Emma else "Emma" if Emma>Gunnar else "Tie")
