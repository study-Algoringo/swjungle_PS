import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for i in range(t):
    n = int(input())
    chass = [[0]* n for _ in range(n)]
    a,b = map(int, input().split())
    A,B = map(int, input().split())
    if a==A and b ==B:
        print(0)
        continue
    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [-1,1,-2,2,-2,2,-1,1]
    que = deque([])
    que.append([a,b])
    chass[a][b] = 1
    
    while que:
        x, y = que.popleft()
        if x == A and y == B:
            print(chass[x][y]-1)
            break
            
        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx >= 0 and nx < n and ny >= 0 and ny< n:
                if not chass[nx][ny]:
                    chass[nx][ny] = chass[x][y] + 1
                    que.append([nx,ny])
                    

    
        
