# 1303 전쟁 - 전투
# b랑 w 따로 bfs로 탐색

from collections import deque

war = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
power = [0 for _ in range(2)]

n, m = map(int, input().split())
for i in range(m):
    war.append(list(input()))

def W_bfs(x, y):
    que = deque()
    que.append((x, y))
    war[x][y] = -1
    cnt = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if war[nx][ny] == "W":
                war[nx][ny] = -1
                que.append((nx, ny))
                cnt += 1
    return cnt * cnt


def B_bfs(x, y):
    que = deque()
    que.append((x, y))
    war[x][y] = -1
    cnt = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if war[nx][ny] == "B":
                war[nx][ny] = -1
                que.append((nx, ny))
                cnt += 1
    return cnt * cnt

for i in range(m):
    for j in range(n):
        if war[i][j] == "W":
            power[0] += W_bfs(i, j)
        if war[i][j] == "B":
            power[1] += B_bfs(i, j)
print(" ".join(map(str, power)))
