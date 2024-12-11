from functools import cache
with open("11.txt") as r:
    stones = tuple(map(int, r.readline().rstrip().split()))

def check(num):
    if not num:
        return tuple([1])
    elif len(str(num)) % 2 == 0:
        num_str = str(num)
        l = len(num_str)
        return int(num_str[:l//2]), int(num_str[l//2:])
    else:
        return tuple([num*2024])

@cache
def solve(stones, blinks):
    if not blinks:
        return len(stones)
    res = 0
    for num in stones:
        res += int(solve(check(num), blinks-1))
    return res
print(solve(stones, 25))
print(solve(stones, 75))