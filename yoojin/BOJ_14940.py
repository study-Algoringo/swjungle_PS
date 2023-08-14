import sys
from collections import deque
read = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, read().split())
ground = [list(map(int, read().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
distance = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if ground[i][j] == 2:
            rx, ry = i, j

def bfs(sx, sy):
    queue = deque([(sx, sy)])
    visited[sx][sy] = 0

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if ground[nx][ny] == 0:
                    visited[nx][ny] = 0
                if ground[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1
    return

bfs(rx, ry)
for i in range(n):
    for j in range(m):
        if ground[i][j] == 0:
            print(0, end = ' ')
        else:
            print(visited[i][j], end = ' ')
    print()