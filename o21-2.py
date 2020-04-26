from collections import deque


class Football:
    def __init__(self, city, team):
        self.city = city
        self.team = deque(team)

    def del_player(self, name):
        self.team.remove(name)

    def add_player(self, name):
        self.team.append(name)


players = {}
teams = {}
n, m = [int(i) for i in input().split()]
for i in range(n):
    a = input().split()
    teams[a[0]] = Football(a[1], a[2:])
    for j in a[2:]:
        players.update({j: teams[a[0]]})

for i in range(m):
    a = input().split()
    if len(a) == 1:
        for j in teams:
            if a[0] in teams[j].team:
                teams[j].del_player(a[0])
    elif len(a) == 2:
        teams[a[1]].add_player(a[0])
    else:
        teams[a[1]].del_player(a[0])
        teams[a[2]].add_player(a[0])
print('\n'.join(sorted(list(set(teams[i].city for i in teams if len(teams[i].team) >= 5)))))
