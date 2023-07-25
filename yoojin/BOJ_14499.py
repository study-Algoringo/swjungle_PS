import sys
read = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

n, m, x, y, k = map(int, read().split())
board = []
dice = [0] * 6

def turn(dir):
    a, b, c, d, e, f = dice[0:6]
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for _ in range(n):
    board.append(list(map(int, read().split())))

dir = list(map(int, read().split()))

nx, ny = x, y
for i in dir:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    turn(i)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0
    print(dice[0])  