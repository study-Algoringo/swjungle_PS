## 시간 초과
import sys
sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
block = []

# 0인 블록
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            block.append([i,j])

# row 확인
def check_row(x,data):
    for i in range(9):
        if sudoku[x][i] == data:
            return False
    return True

# col 확인
def check_col(y,data):
    for i in range(9):
        if sudoku[i][y] == data:
            return False
    return True

# block 내 확인
def check_block(x,y,data):
    nx = (x//3)*3
    ny = (y//3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[nx+i][ny+j] == data:
                return False
    return True

def dfs(idx):
    if idx == len(block):
        for _ in range(9):
            print(*sudoku[_])
        exit(0)

    for j in range(1,10):
        x = block[idx][0]
        y = block[idx][1]
        if check_block(x,y,j) and check_col(y,j) and check_row(x,j):
            sudoku[x][y] = j
            dfs(idx+1)
            sudoku[x][y] = 0  
dfs(0)