# if there's an obstacle at (i, j): o[i][j] = True
o = []
poss_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
starting_pos = []
rows = 0
def turn(dir):
    if dir == poss_dirs[0]:
        return poss_dirs[1]
    if dir == poss_dirs[1]:
        return poss_dirs[2]
    if dir == poss_dirs[2]:
        return poss_dirs[3]
    if dir == poss_dirs[3]:
        return poss_dirs[0]
with open("6.txt") as r:
    lines = r.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()
    row = []
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            row.append(True)
        else:
            row.append(False)
            if lines[i][j] == "^":
                starting_pos = [i, j]
    o.append(row)
rows = len(o)
cols = len(o[0])
def traverse(curr, dir, obs=None):
    i, j = curr
    visited = set()
    v_cdirs = set()
    v_cdirs.add((i, j, dir))
    while 0 <= i < rows and 0 <= j < cols:
        visited.add((i, j))
        ni, nj = i+dir[0], j+dir[1]
        if (0 <= ni < rows and 0 <= nj < cols) and (o[ni][nj] or (obs and (ni, nj) == obs)):
            dir = turn(dir)
        else:
            i, j = ni, nj
        if (i, j, dir) in v_cdirs:
            return True, visited
        v_cdirs.add((i, j, dir))
    return False, visited
nah, tos = traverse(starting_pos, poss_dirs[0])
print("Visited:", len(tos))
ans = 0
tos = tos - {tuple(starting_pos)}
for ob in tos:
    if ob != starting_pos:
        if traverse(starting_pos, poss_dirs[0], ob)[0]:
            ans += 1
print("Possible placements:", ans)