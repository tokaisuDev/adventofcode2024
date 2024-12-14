import re
import numpy as np
with open("13.txt") as r:
    data = r.readlines()
data = "".join(data)
data = list(re.findall(r"\d+", data))
data = list(map(int, data))
i = 0
ans1 = 0
ans2 = 0
while i < len(data):
    a_x = data[i]
    a_y = data[i+1]
    b_x = data[i+2]
    b_y = data[i+3]
    target_x, target_y = data[i+4], data[i+5]
    root1 = np.linalg.solve(np.array([[a_x, b_x], [a_y, b_y]]), np.array([target_x, target_y]))
    root1 = list(map(round, root1))
    if root1[0]*a_x + root1[1]*b_x == target_x and root1[0]*a_y+root1[1]*b_y == target_y:
        ans1 += round(root1[0])*3+round(root1[1])
    target_x += 10000000000000
    target_y += 10000000000000
    root2 = np.linalg.solve(np.array([[a_x, b_x], [a_y, b_y]]), np.array([target_x, target_y]))
    root2 = list(map(round, root2))
    if root2[0]*a_x + root2[1]*b_x == target_x and root2[0]*a_y+root2[1]*b_y == target_y:
        ans2 += round(root2[0])*3+round(root2[1])
    i += 6
print(ans1)
print(ans2)