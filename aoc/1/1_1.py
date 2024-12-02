l1 = []
l2 = []
with open("1.txt", "r") as o:
    for data in o.readlines():
        t1, t2 = list(map(int, data.split()))
        l1.append(t1)
        l2.append(t2)
l1.sort()
l2.sort()
ans = 0
for i in range(len(l1)):
    ans += abs(l1[i]-l2[i])
print(ans)