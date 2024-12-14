import re
import PIL
import PIL.Image
grid = [[0 for _ in range(101)] for _ in range(103)]
rows = 103
cols = 101
with open("14.txt") as r:
    data = r.readlines()
for line in data:
    px,py,dx,dy = list(map(int, re.findall(r"(?:\-)?\d+", line)))
    grid[(py+100*dy)%rows][(px+100*dx)%cols] += 1
mid_row = rows//2
mid_col = cols//2
ans = 1
cnt = 0
for i in range(mid_row):
    for j in range(mid_col):
        cnt += grid[i][j]
ans *= cnt
cnt = 0
for i in range(mid_row):
    for j in range(mid_col+1, cols):
        cnt += grid[i][j]
ans *= cnt
cnt = 0
for i in range(mid_row+1, rows):
    for j in range(mid_col):
        cnt += grid[i][j]
ans *= cnt
cnt = 0
for i in range(mid_row+1, rows):
    for j in range(mid_col+1, cols):
        cnt += grid[i][j]
ans *= cnt
print(ans)
# PART 2
secs = 0
while True:
    img = PIL.Image.new(mode="RGB", size=(cols, rows), color=(0, 0, 0))
    if secs > 10000:
        break
    for line in data:
        px,py,dx,dy = list(map(int, re.findall(r"(?:\-)?\d+", line)))
        img.putpixel(((px+dx*secs)%cols, (py+dy*secs)%rows), (255,255,255))
    img.save("photos/"+str(secs)+".jpg")
    secs += 1