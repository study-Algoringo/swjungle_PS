# 현재 위치 1,1 / 상대 위치 n,m
# 동, 서, 남, 북 방향으로 한칸씩 이동 
from collections import deque
import sys
def solution(maps):
    # n : 행, m : 열
    n = len(maps)
    m = len(maps[0])

    answer = (n*m)+1

    visited = [[-1]*m for _ in range(n)] 

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    que = deque([[1,0,0]])
    visited[0][0] = 1
    while que:
        cnt,x,y = que.popleft()
        if x == n-1 and y == m-1:
            answer = min(answer,cnt)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 and visited[nx][ny]==-1:
                visited[nx][ny]=cnt+1
                que.append([cnt+1,nx,ny])

    if answer == (n*m)+1:
        answer = -1

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))