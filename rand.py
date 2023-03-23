import random as r

teamlist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]

team = []

for i in range(0, 15):
    team.append(teamlist.pop(r.randrange(0, 15-i)))

print(team)