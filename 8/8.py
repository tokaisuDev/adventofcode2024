from math import gcd
with open("8.txt") as r:
    grid = r.readlines()
rows = len(grid)
antennas = []
for i in range(rows):
    grid[i] = grid[i].rstrip()
    for j in range(len(grid[i])):
        if grid[i][j] != '.':
            antennas.append((i, j))
cols = len(grid[0])
output = [[char for char in grid[i]] for i in range(rows)] # for debugging
mode = int(input("Which half?"))
antinodes = set()
a = len(antennas)
for i in range(a):
    for j in range(i+1, a):
        p1 = antennas[i]
        p2 = antennas[j]
        if grid[p1[0]][p1[1]] == grid[p2[0]][p2[1]]:
            di = p2[0]-p1[0]
            dj = p2[1]-p1[1]
            if mode == 1:
                if 0 <= p1[0]-di < rows and 0 <= p1[1]-dj < cols:
                    antinodes.add((p1[0]-di, p1[1]-dj))
                if 0 <= p2[0]+di < rows and 0 <= p1[1]+dj < cols:
                    antinodes.add((p2[0]+di, p2[1]+dj))
            if mode == 2:
                g = gcd(di, dj)
                di //= g
                dj //= g
                k = 1
                while 0 <= p1[0]-di*k < rows and 0 <= p1[1]-dj*k < cols:
                    if grid[p1[0]-di*k][p1[1]-dj*k] == ".":
                        output[p1[0]-di*k][p1[1]-dj*k] = "#"
                    antinodes.add((p1[0]-di*k, p1[1]-dj*k))
                    k += 1
                k = 1
                while 0 <= p1[0]+di*k < rows and 0 <= p1[1]+dj*k < cols:
                    if grid[p1[0]+di*k][p1[1]+dj*k] == ".":
                        output[p1[0]+di*k][p1[1]+dj*k] = "#"
                    antinodes.add((p1[0]+di*k, p1[1]+dj*k))
                    k += 1
                antinodes.add(p1)
print("# of antinodes:", len(antinodes))