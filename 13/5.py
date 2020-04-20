word = []
n = int(input())
for i in range(n):
    w = input()
    word.append(w)
for i in range(n):
    for j in range(i + 1, n):
        if word[i] > word[j]:
            word[i], word[j] = word[j], word[i]
word.sort(key=len)
for e in word:
    print(e)
