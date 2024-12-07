def valid(nums, val, pos, flag, curr=0):
    if pos == len(nums):
        return curr == val
    elif pos == 0:
        return valid(nums, val, pos+1, flag, nums[pos])
    else:
        res = valid(nums, val, pos+1, flag, curr*nums[pos]) or valid(nums, val, pos+1, flag, curr+nums[pos])
        if flag:
            res = res or valid(nums, val, pos+1, flag, int(str(curr)+str(nums[pos])))
        return res

ans = 0
mode = int(input("Which half? "))
flag = mode == 2
with open("7.txt") as r:
    for line in r.readlines():
        line = line.rstrip()
        data = line.split(" ")
        res = int(data[0].replace(":", ""))
        nums = list(map(int, data[1:]))
        if valid(nums, res, 0, flag):
            print(res)
            ans += res
print(ans)