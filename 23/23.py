def score(s, n=1):
    global scoring
    if s == 'Яблочко':
        return 50
    elif s == 'зелёное кольцо':
        return 25
    else:
        return scoring[s][n]
