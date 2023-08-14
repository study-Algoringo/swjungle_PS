import sys
from collections import deque
read = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, read().split())
visited = [[False] * m for _ in range(n)]
grid = [list(map(int, read().split())) for _ in range(n)]
h, w, Sr, Sc, Fr, Fc = map(int, read().split())
Sr, Sc, Fr, Fc = Sr - 1, Sc - 1, Fr - 1, Fc - 1

walls = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            walls.append((i, j))

def check(x, y):
    for wx, wy in walls:
        if x <= wx < x + h and y <= wy < y + w:
            return False
    return True

def bfs(Sr, Sc):
    queue = deque([(Sr, Sc, 0)])
    
    while queue:
        cx, cy, cnt = queue.popleft()
        visited[cx][cy] = True

        if cx == Fr and cy == Fc:
            print(cnt)
            return
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n - h + 1 and 0 <= ny < m - w + 1 and not visited[nx][ny]:
                # 직사각형 안에 1이 있지 않으면
                if check(nx, ny):
                    queue.append((nx, ny, cnt + 1))
                    visited[nx][ny] = True
    print(-1)
    return

bfs(Sr, Sc)