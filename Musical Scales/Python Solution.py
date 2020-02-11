#the list of notes, doubled so no need to wrap
notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#","A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]

#takes in input and clears any empty char just in case
x = int(input())
song = set(input().split(' '))
if ('' in song):
    song.remove('')

#goes through each major key and checks if the notes are all in that key
out = []
for i in range(12):
    tmpNotes = [notes[i],notes[i+2],notes[i+4],notes[i+5],notes[i+7],notes[i+9],notes[i+11]]
    if(song.issubset(set(tmpNotes))):
        out.append(notes[i])

#prints the output
print(' '.join(out) if len(out)>0 else "none")
