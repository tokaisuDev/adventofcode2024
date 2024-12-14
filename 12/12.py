with open("12.txt") as r:
    data = r.readlines()
visited = []
for i in range(len(data)):
    data[i] = data[i].rstrip()
    visited.append([False for _ in range(len(data[i]))])
rows = len(data)
cols = len(data[0])
a = 0
p = 0
edge_points = [set() for _ in range(4)]

def ff(i, j, veg, dir):
    global a, p, edge_points
    if i < 0 or i >= rows or j < 0 or j >= cols or data[i][j] != veg:
        p += 1
        if dir == '^':
            edge_points[0].add((i, j))
        elif dir == "v":
            edge_points[1].add((i, j))
        elif dir == ">":
            edge_points[2].add((i, j))
        else:
            edge_points[3].add((i, j))
        return
    if visited[i][j]:
        return
    visited[i][j] = True
    a += 1
    ff(i+1, j, veg, "v")
    ff(i-1, j, veg, "^")
    ff(i, j+1, veg, ">")
    ff(i, j-1, veg, "<")

def process(points, mode):
    sides = 0
    if mode == 0:
        t = 1
        k = 0
    elif mode == 1:
        t = 0
        k = 1
    points = list(sorted(points, key=lambda x: x[k]))
    # print(points)
    mark = [False for _ in range(len(points))]
    for i in range(len(points)):
        if not mark[i]:
            sides += 1
            check_coord = points[i][t]
            curr_coord = points[i][k]
            for j in range(i+1, len(points)):
                if points[j][t] == check_coord and points[j][k]-curr_coord == 1:
                    mark[j] = True
                    curr_coord += 1
    return sides

ans = 0
ans2 = 0
for i in range(0, rows):
    for j in range(0, cols):
        # print(f"i: {i}, j: {j}")
        if not visited[i][j]:
            print(data[i][j])
            edge_points = [set() for _ in range(4)]
            a = 0
            p = 0
            ff(i, j, data[i][j], "")
            sides = 0
            for k in range(2):
                sides += process(edge_points[k], 1)
            for k in range(2, 4):
                sides += process(edge_points[k], 0)
            print(a)
            print(p)
            ans += a*p
            ans2 += sides*a
            # print(visited)
print(ans)
print(ans2)