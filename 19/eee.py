def print_long_words(text):
    for i in range(len(text)):
        if not text[i].isalpha() and text[i] != ' ':
            text[i] = text[i].replace(text[i], ' ')
    text = text.split()
    for i in text:
        s = 0
        for j in 'аеёиоуыэюяaeiouy':
            if i.count(j) > 0:
                s += i.count(j)
        if s >= 4:
            print(i)
