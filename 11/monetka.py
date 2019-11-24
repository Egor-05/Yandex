p = input()
s = 0
st = 0
for i in p:
    if i == chr(1086):
        s += 1
    else:
        if s > st:
            st = s
        s = 0
if s > st:
    st = s
print(st)
