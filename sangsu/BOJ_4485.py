import sys
input = sys.stdin.readline
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
problem = 0
while 1:
    
    if int(input()) == 0:
        break
    
    else:
        problem += 1
        n = int(input())
        cave = []
        costs = list([int(1e9)]*n for _ in range(n))
        
        for i in range(n):
            cave.append(list(map(int, input().split())))
        costs[0][0] = cave[0][0]
        que = deque()
        que.append((0,0))
        while que:
            x,y = que.popleft()
            for j in range(4):
                nx = x +dx[i]
                ny = y +dy[i]
                if 0 <=nx <n and 0 <=ny <n:
                    if costs[nx][ny] < costs[x][y] + cave[nx][ny]:
                        costs[nx][ny] = costs[x][y] + cave[nx][ny]
                        que.append((nx, ny))
                        
        print("problem",problem,":", costs[n-1][n-1])
            
        