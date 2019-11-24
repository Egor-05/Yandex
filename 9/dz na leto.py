hl = set()
hl_input = int(input())
ht = set()
ht_input = int(input())
for i in range(hl_input):
    book = input()
    hl.add(book)
for i in range(ht_input):
    book = input()
    ht.add(book)
    if book in hl:
        print('YES')
    else:
<<<<<<< HEAD
        print('NO')
=======
        print('NO')
>>>>>>> efd9a8d66c8a956ef6f0c0483298939b706250f8
