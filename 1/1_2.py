l1 = []
l2 = dict()
with open("1.txt", "r") as o:
    for data in o.readlines():
        a, b = list(map(int, data.split()))
        if b in l2:
            l2[b] += 1
        else:
            l2[b] = 1
        l1.append(a)
ans = 0
print(l1, l2)
for k in l1:
    if k in l2:
        ans += k*l2[k]
print(ans)