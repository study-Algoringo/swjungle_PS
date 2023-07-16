import sys
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [read().strip() for i in range(m)]
my_score = 0; enemy_score = 0

# 방문 배열 만들기
visited = [[0] * n for i in range(m)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(y, x, char):
    count = 1
    visited[y][x] = 1
    # 상, 하, 좌, 우를 각각 한 번씩 방문 - 같은 색인 경우 go
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx]:
            if graph[ny][nx] == char:
                count += dfs(ny, nx, char)
    return count

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] == 'W':
                my_score += dfs(i, j, 'W') ** 2
            else:
                enemy_score += dfs(i, j, 'B') ** 2
print(my_score, enemy_score)