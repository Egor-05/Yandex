soups = ['щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански']
a = int(input())
for i in range(a):
    print(soups[i % 5])