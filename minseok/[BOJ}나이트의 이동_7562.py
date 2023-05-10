import sys
input = sys.stdin.readline
from collections import deque



def bfs(x, y):
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    q = deque()
    q.append([x,y])
    
    while q:
        x,y = q.popleft()
        if x == goalx and y == goaly:
            print(chess[goalx][goaly])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if  l>nx>=0 and l>ny>=0 and chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                q.append([nx,ny])
    

n = int(input())

for j in range(n):
    l = int(input())
    startx, starty = map(int, input().split())
    goalx, goaly = map(int, input().split())
    chess = [[0]*l for _ in range(l)]
    bfs(startx,starty)



