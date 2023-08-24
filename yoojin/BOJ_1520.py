import sys
sys.setrecursionlimit(10 ** 9)
read = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, read().split())
grid = list(list(map(int, read().split())) for _ in range(m))
memo = [[-1] * (n + 1) for _ in range(m + 1)]

# (0, 0)에서부터 시작하여 오른쪽 아래까지 가는 경로
# def bfs(start):
#     global cnt
#     x, y = start
#     queue = deque([start])
#     visited[x][y] = 1

#     while queue:
#         cx, cy = queue.popleft()

#         for i in range(4):
#             nx = cx + dx[i]
#             ny = cy + dy[i]
#             if 0 <= nx < m and 0 <= ny < n:
#                 if nx == m - 1 and ny == n - 1:
#                         cnt += 1
#                 if not visited[nx][ny] and grid[cx][cy] > grid[nx][ny]:
#                     queue.append((nx, ny))
#                     visited[nx][ny] = 1

def dfs(x, y):
    if x == m - 1 and y == n - 1:
          return 1
    
    if memo[x][y] != -1:
         return memo[x][y]
    
    cnt = 0
    for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if 0 <= nx < m and 0 <= ny < n and grid[x][y] > grid[nx][ny]:
                cnt += dfs(nx, ny)
    memo[x][y] = cnt
    return cnt

print(dfs(0, 0))