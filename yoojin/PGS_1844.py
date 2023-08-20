from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = 0; m = 0

def solution(maps):
    answer = 0
    global n, m
    n = len(maps); m = len(maps[0])
    visited = [[0] * (m + 1) for _ in range(n + 1)]
    
    answer = bfs(1, 1, visited, maps)
    return answer

def bfs(x, y, visited, maps):
    # bfs로 시작점으로부터 우측 하단(목적지)까지의 최단 거리 구하기
    queue = deque([(x, y, 1)])
    visited[x][y] = 1
    
    while queue:
        cx, cy, cnt = queue.popleft()
        
        if cx == n and cy == m:
            return cnt
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 < nx <= n and 0 < ny <= m and not visited[nx][ny]:
                if maps[nx - 1][ny - 1] == 1:
                    queue.append((nx, ny, cnt + 1))
                    visited[nx][ny] = 1
    return -1