mode = int(input("Which half? "))
disk = []
with open("9.txt") as r:
    m = r.readline()
size = 0
files = 0
for i in range(len(m)):
    l = int(m[i])
    if i % 2 == 0:
        disk.extend([files]*l)
        files += 1
    else:
        disk.extend([-1]*l)
    size += l
# for k in disk:
#     if k == -1:
#         print(".", end="")
#     else:
#         print(k, end="")
# print()
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
    next = files-1
    while next >= 0:
        i = size-1
        end = size-1
        start = -1
        found = False
        # for k in disk:
        #     if k == -1:
        #         print(".", end="")
        #     else:
        #         print(k, end="")
        # print()
        # find file
        while i >= 0:
            if disk[i] == next:
                if not found:
                    found = True
                    end = i
            elif disk[i] != next:
                if found:
                    start = i+1
                    break
            i -= 1
        # print(start, end)
        file_size = end-start
        # find free spaces in the disk that the file can fit
        start_free = 0
        end_free = 0
        i = 0
        found = False
        fit = False
        while i < size:
            if disk[i] == -1:
                if not found:
                    found = True
                    start_free = i
            else:
                if found:
                    end_free = i-1
                    found = False
                    if end_free-start_free >= file_size and start > end_free:
                        fit = True
                        break
            i += 1
        if fit:
            i = start
            j = start_free
            while i <= end and j <= end_free:
                tmp = disk[i]
                disk[i] = disk[j]
                disk[j] = tmp
                i += 1
                j += 1
            # print(next)
            # print(start_free, end_free)
            # for k in disk:
            #     if k == -1:
            #         print(".", end="")
            #     else:
            #         print(k, end="")
            # print()
        next -= 1
    for i in range(size):
        if disk[i] != -1:
            ans += disk[i]*i
print(ans)