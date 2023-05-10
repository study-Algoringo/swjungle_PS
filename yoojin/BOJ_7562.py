from collections import deque
import sys
read = sys.stdin.readline

d = [[1, 2], [2, 1], [2, -1], [1, -2],
     [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

def bfs(l, sx, sy, ex, ey):
    q = deque([])
    visited = list([0] * l for _ in range(l))
    q.append((sx, sy))
    while q:
        cx, cy = q.popleft()
        if cx == ex and cy == ey:
            return visited[cx][cy]
        for n in d:
            nx = cx + n[0]
            ny = cy + n[1]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))

tc = int(read())
for _ in range(tc):
    l = int(read())
    sx, sy = map(int, read().split())
    ex, ey = map(int, read().split())
    print(bfs(l, sx, sy, ex, ey))