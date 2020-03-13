def same_by(characteristic, objects):
    a = set()
    for i in objects:
        a.add(characteristic(i))
    if len(a) == 1 or len(a) == 0:
        return True
    else:
        return False
