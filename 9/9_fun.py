# DO NOT DO THIS AT HOME. THIS COULD TAKE UP TO ~49HRS.
mode = int(input("Which half? "))
disk = []
blanks = []
files_ = []
with open("9.txt") as r:
    m = r.readline()
size = 0
files = 0
for i in range(len(m)):
    l = int(m[i])
    if i % 2 == 0:
        disk.extend([files]*l)
        files_.append((size, size+l-1))
        files += 1
    else:
        blanks.append((size, size+l-1))
        disk.extend([-1]*l)
    size += l
print(files_)
i = 0
j = size-1
ans = 0
if mode == 1:
    while i < j:
        if disk[i] != -1:
            ans += disk[i]*i
            i += 1
        elif disk[j] == -1:
            j -= 1
        else:
            tmp = disk[j]
            disk[j] = disk[i]
            disk[i] = tmp
            ans += disk[i]*i
            i += 1
            j -= 1
    while disk[i] != -1:
        ans += disk[i]*i
        i += 1
elif mode == 2:
    for i in range(files-1, -1, -1):
        for j in range(len(blanks)):
            curr_file = files_[i]
            if curr_file[1]-curr_file[0] <= blanks[j][1]-blanks[j][0] and curr_file[1] >= blanks[j][0]:
                disk[curr_file[0]:curr_file[1]+1], disk[blanks[j][0]:min(blanks[j][0]+curr_file[1]-curr_file[0], blanks[j][1])+1] = disk[blanks[j][0]:min(blanks[j][0]+curr_file[1]-curr_file[0], blanks[j][1])+1], disk[curr_file[0]:curr_file[1]+1]
                blanks = []
                start = False
                x = 0
                for i in range(size):
                    if disk[i] == -1:
                        if not start:
                            x = i
                            start = True
                    else:
                        if start:
                            start = False
                            blanks.append((x, i-1))
                print(blanks)
                for k in disk:
                    if k == -1:
                        print(".", end="")
                    else:
                        print(k, end="")
                print()
                break
    for i in range(size):
        if disk[i] != -1:
            ans += disk[i]*i
print(ans)