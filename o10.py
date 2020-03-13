from collections import defaultdict


indsongs = {}
songs = defaultdict(int)
for i in range(int(input())):
    songs[input()] += 1
a = list(songs.keys())
for i in a:
    indsongs[songs[i]] = a.index(i)

