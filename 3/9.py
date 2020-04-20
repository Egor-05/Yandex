h1 = int(input())
h2 = int(input())
h3 = int(input())
if h1 < h2:
    h1, h2 = h2, h1
if h2 < h3:
    h2, h3 = h3, h2
if h1 < h2:
    h1, h2 = h2, h1
print(h1)
print(h2)
print(h3)