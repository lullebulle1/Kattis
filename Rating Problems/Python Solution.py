judges, voted = list(map(int, input().split()))
totVotes = sum([int(input()) for i in range(voted)])

low = totVotes + -3*(judges-voted)
high = totVotes + 3*(judges-voted)

print (low/judges, high/judges)
