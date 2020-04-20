word2 = input()
while 1:
    word1 = input()
    if word2[len(word2) - 1] != word1[0]:
        print(word1)
        break
    word2 = input()
    if word1[len(word1) - 1] != word2[0]:
        print(word2)
        break