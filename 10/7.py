word = input()
for i in range(len(word) - 1):
    print(ord(word[i]), end=', ')
print(ord(word[len(word) - 1]))
