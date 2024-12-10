m = []
with open("10.txt") as r:
    data = r.readlines()
for line in data:
    line = line.rstrip()
    row = []
    for char in line:
        row.append(int(char))
    m.append(row)
rows = len(m)
cols = len(m[0])

def bfs(i, j):
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    score = 0
    # format: row, col, expected value
    queue = [(i, j, 0)]
    while queue:
        # print(queue)
        curr = queue.pop(0)
        if 0 <= curr[0] < rows and 0 <= curr[1] < cols and m[curr[0]][curr[1]] == curr[2] and not visited[curr[0]][curr[1]]:
            # print("mewing")
            visited[curr[0]][curr[1]] = True
            if curr[2] == 9:
                score += 1
                continue
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                queue.append((curr[0]+i, curr[1]+j, curr[2]+1))
    return score

def rat(i, j):
    rats = 0
    queue = [(i, j, 0)]
    while queue:
        curr = queue.pop(0)
        if 0 <= curr[0] < rows and 0 <= curr[1] < cols and m[curr[0]][curr[1]] == curr[2]:
            if curr[2] == 9:
                rats += 1
                continue
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                queue.append((curr[0]+i, curr[1]+j, curr[2]+1))
    return rats

ans = 0
ratings = 0
for i in range(rows):
    for j in range(cols):
        if m[i][j] == 0:
            ans += bfs(i, j)
            ratings += rat(i, j)
print("Total score:", ans)
print("Total ratings:", ratings)