import sys
from collections import deque
read = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, read().split())
visited = [[0] * m for _ in range(n)]
grid = [list(map(int, read().split())) for _ in range(n)]
h, w, Sr, Sc, Fr, Fc = map(int, read().split())
Sr, Sc, Fr, Fc = Sr - 1, Sc - 1, Fr - 1, Fc - 1

def bfs(Sr, Sc, visited):
    answer = -1
    queue = deque([])
    queue.append((Sr, Sc))
    visited[Sr][Sc] = 1
    
    while queue:
        cx, cy = queue.popleft()
        if cx == Fr and cy == Fc:
            answer = visited[cx][cy]
            break
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n - h and 0 <= ny < m - w and not visited[nx][ny]:
                # 직사각형 안에 1이 있지 않으면
                flag = 1
                for i in range(nx, nx + h):
                    for j in range(ny, ny + w):
                        if grid[i][j] == 1:
                            flag = 0
                            break
                if flag == 1 :
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1

    return answer

print(bfs(Sr, Sc, visited))