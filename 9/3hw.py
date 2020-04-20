nw = int(input())
of = set()
w = set()
for i in range(nw):
    now = input()
    d = len(w)
    w.add(now)
    if d == len(w):
        of.add(now)
print(nw - len(w) + len(of))
