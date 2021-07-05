import math

def position(p, s, k):
    if s == 'UP': p[1] += k
    elif s == 'DO': p[1] -= k
    elif s == 'R': p[0] += k
    elif s == 'L': p[0] -= k
    return p

file = open('file.in', 'r')
positions = dict()
for row in file:
    r, s, k = row.strip().split()
    k = int(k)
    if r not in positions:
        positions[r] = position([0, 0], s, k)
    else:
        positions[r] = position(positions[r], s, k)

for k in sorted(positions.keys()):
    print(k, end=' ')
    print(math.sqrt(pow(positions[k][0], 2) + pow(positions[k][1], 2)))





















