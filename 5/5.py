# all pages that are needed to be printed after p: afters[p]
afters = dict()
# pages that has to be printed BEFORE p: befores[p]
befores = dict()
def main():
    mode = int(input("Which half? "))
    ans = 0
    with open("5.txt") as r:
        for line in r.readlines():
            line = line.rstrip()
            if not line:
                continue
            if "|" in line:
                a, b = list(map(int, line.split("|")))
                if a in afters:
                    afters[a].append(b)
                else:
                    afters[a] = [b]
                if b in befores:
                    befores[b].append(a)
                else:
                    befores[b] = [a]
            else:
                update = list(map(int, line.split(",")))
                good = is_correct(update)
                if good and mode == 1:
                    ans += update[len(update)//2]
                elif not good and mode == 2:
                    while not is_correct(update):
                        correct(update)
                    ans += update[len(update)//2]
    print(ans)

def correct(update):
    for i in range(len(update)):
        to = i
        if update[i] in afters:
            for after in afters[update[i]]:
                if after in update and update.index(after) < i:
                    to = min(to, update.index(after))
            update[i], update[to] = update[to], update[i]

def is_correct(update):
    good = True
    for i in range(len(update)):
        if update[i] not in afters:
            continue
        for after in afters[update[i]]:
            if after in update and update.index(after) < i:
                good = False
                break
    return good

if __name__ == "__main__":
    main()