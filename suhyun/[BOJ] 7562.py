import sys
from collections import deque
N = int(sys.stdin.readline())
for _ in range(N):
    I = int(sys.stdin.readline())
    a,b = map(int,sys.stdin.readline().split())
    rx,ry = map(int,sys.stdin.readline().split())
    visited = [[False]*I for _ in range(I)]
    visited[a][b] = True
    dx = [-1,1,-2,2,-1,1,-2,2]
    dy = [-2,-2,-1,-1,2,2,1,1]
    que = deque([[a,b,0]])
    answer = 0
    while que:
        x,y,c = que.popleft()

        if x == rx and y == ry:
            answer = c
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<I and 0<=ny<I and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append([nx,ny,c+1])
    print(answer)