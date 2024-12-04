class Letter:
    def __init__(self, r, c, r_dir, c_dir, index):
        self.r = r
        self.c = c
        self.r_dir = r_dir
        self.c_dir = c_dir
        self.index = index

word = "XMAS"
with open("4.txt", "r") as file:
    text = file.readlines()
text = [line.rstrip() for line in text]
cols = len(text[0])
rows = len(text)

def find(r, c):
    cnt = 0
    queue = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not i == j == 0:
                queue.append(Letter(r+i, c+j, i, j, 1))
    while queue:
        v = queue.pop()
        if v.index == 4:
           cnt += 1
           continue
        if 0 <= v.r < rows and 0 <= v.c < cols and text[v.r][v.c] == word[v.index]:
            queue.append(Letter(v.r+v.r_dir, v.c+v.c_dir, v.r_dir, v.c_dir, v.index+1))
    return cnt

def is_X_MAS(r, c):
    diag1 = ["M", "S"]
    diag2 = diag1.copy()
    if r > 0 and c > 0 and text[r-1][c-1] in diag1:
        diag1.remove(text[r-1][c-1])
        if r < rows-1 and c < cols-1 and text[r+1][c+1] in diag1:
            if r > 0 and c < cols-1 and text[r-1][c+1] in diag2:
                diag2.remove(text[r-1][c+1])
                if r < rows-1 and c > 0 and text[r+1][c-1] in diag2:
                    return True
    return False
            
def main():
    mode = int(input()) # 1 = xmas, 2 = x-mas
    ans = 0
    for i in range(rows):
        for j in range(cols):
            if text[i][j] == "X" and mode == 1:
                ans += find(i, j)
            elif text[i][j] == "A" and mode == 2:
                ans += is_X_MAS(i, j)
                
    print(ans)
                
if __name__ == "__main__":
    main()
