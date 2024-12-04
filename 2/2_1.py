ans = 0
with open("2.txt") as r:
    for data in r.readlines():
        l = list(map(int, data.split()))
        dir = -1 # 1 means increasing, -1 means decreasing
        good = True
        for i in range(len(l)):
            if i == 1:
                if l[i-1] > l[i] and 1 <= abs(l[i-1]-l[i]) <= 3:
                    dir = -1
                elif l[i-1] < l[i] and 1 <= abs(l[i-1]-l[i]) <= 3:
                    dir = 1
                else:
                    good = False 
                    break
            elif i > 1:
                if (l[i-1] < l[i] and dir == -1) or (l[i-1] > l[i] and dir == 1) or 1 > abs(l[i-1]-l[i]) or abs(l[i-1]-l[i]) > 3:
                    good = False
                    break
            last = l[i]
        ans += good
print(ans)                
        