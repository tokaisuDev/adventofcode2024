import re

check_pattern = r"mul\(\d{1,3},\d{1,3}\)|do(?:n't)?\(\)"

def finder(text):
    founds = re.findall(check_pattern, text)
    return list(founds)

def mul(x, y):
    return x*y

def main():
    ans = 0
    with open("3.txt") as file:
        activated = True
        for line in file.readlines():
            for func in finder(line):
                if func == "do()":
                    activated = True
                elif func == "don't()":
                    activated = False
                else:
                    if activated:
                        ans += eval(func)
    print(ans)
    
if __name__ == "__main__":
    main()