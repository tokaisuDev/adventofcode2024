o = []
visited = []
poss_dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dir = [-1, 0]
curr = [-1, -1]
starting_pos = [-1, -1]
rows = 0
obs = []
turns_cnt = 0

with open("6.txt") as r:
    for line in r.readlines():
        row = []
        row2 = []
        cols = 0
        for char in line.rstrip():
            row2.append(False)
            if char == "#":
                obs.append([rows, cols])
                row.append(True)
            else:
                row.append(False)
                if char == "^":
                    curr = [rows, cols]
                    starting_pos = curr.copy()
            cols += 1
        visited.append(row2)
        o.append(row)
        rows += 1
cols = len(o[0])
mode = int(input("Which half? "))
ans = 0
tos = set() 
while 0 <= curr[0] < rows and 0 <= curr[1] < cols:
    if not visited[curr[0]][curr[1]]:
        tos.add(tuple(curr))
        ans += 1
        visited[curr[0]][curr[1]] = True
    next = [curr[0]+dir[0], curr[1]+dir[1]]
    if 0 <= next[0] < rows and 0 <= next[1] < cols:
        if (o[next[0]][next[1]]):
            turns_cnt += 1
            dir = poss_dirs[turns_cnt % 4]
    curr = [curr[0]+dir[0], curr[1]+dir[1]]
res = 0
# pt.2
for ob in tos:
    if ob == starting_pos:
        continue
    curr = starting_pos
    turns_cnt = 0
    dir = poss_dirs[0]
    loop = False
    v = set()
    o[ob[0]][ob[1]] = True
    while 0 <= curr[0] < rows and 0 <= curr[1] < cols:
        next = [curr[0]+dir[0], curr[1]+dir[1]]
        if 0 <= next[0] < rows and 0 <= next[1] < cols and (o[next[0]][next[1]]):
            turns_cnt += 1
            dir = poss_dirs[turns_cnt % 4]
        else:
            curr = next
        if tuple(curr+dir) in v:
            loop = True
            break
        else:
            v.add(tuple(curr+dir))
    if loop:
        res += 1
    o[ob[0]][ob[1]] = False
if mode == 1:
    print(ans)
elif mode == 2:
    print(res)