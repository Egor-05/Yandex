b = set()
bulls = 0
cows = 0
word1 = input()
word2 = input()
for i in range(len(word1)):
    if word1[i] == word2[i]:
        bulls += 1
        b.add(word1[i])
bu = set(word1)
c = set(word2)
c = (c & bu) - b
print(len(b), len(c))