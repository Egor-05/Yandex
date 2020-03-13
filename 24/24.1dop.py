a = input().split()
vowels = [[]] * len(a)
for i in range(len(a)):
    vowels[i] = [j for j in a[i] if j.lower() in 'аеёиоуыэюя']
res = [i for i in vowels if len(i) == len(vowels[0])]
if len(res) == len(a):
    print('Парам пам-пам')
else:
    print('Пам парам')
