from collections import defaultdict


indsongs = defaultdict(list)
songs = defaultdict(int)
for i in range(int(input())):
    songs[input()] += 1
a = list(songs.keys())
for i in a:
    indsongs[songs[i]].append(i)
s = []
for i in sorted(indsongs, reverse=True):
    for j in sorted(indsongs[i]):
        s.append(j)
for i in range(min(20, len(s))):
    print(f'{i + 1}. {s[i]}')
