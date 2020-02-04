#takes in input
sentence = list(input().split(' '))

#calculates words with ae
wordsWithAE = len([x for x in sentence if "ae" in x])

#finds proportion of words with ae to total words
prop = wordsWithAE/len(sentence)

#prints answer
print("dae ae ju traeligt va" if prop>=.4 else "haer talar vi rikssvenska")

