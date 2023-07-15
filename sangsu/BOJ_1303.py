import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
soldiers = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(m):
    soldier = list(input().strip())
    soldiers.append(soldier)
W_cnt = 0
B_cnt = 0

visited = [[0]*n for _ in range(m)]

def wPower(a,b):
    cnt= 0
    que = deque([(a,b)])
    while que:
        x,y = que.popleft()
        if not visited[y][x]:
            if soldiers[y][x] == "W":
                cnt += 1
                visited[y][x] = 1   
                for p in range(4):
                    nx = x + dx[p]
                    ny = y + dy[p]
                    if 0 <= nx < n and 0 <= ny < m and soldiers[ny][nx] == "W" and not visited[ny][nx]:
                        que.append((nx, ny))
                        
    return (cnt**2)

def BPower(a,b):
    cnt= 0
    que = deque([(a,b)])
    while que:
        x,y = que.popleft()
        if not visited[y][x]:
            if soldiers[y][x] == "B":
                cnt += 1
                visited[y][x] = 1   
                for q in range(4):
                    nx = x + dx[q]
                    ny = y + dy[q]
                    if 0 <= nx < n and 0 <= ny < m and soldiers[ny][nx] == "B" and not visited[ny][nx]:
                        que.append((nx, ny))
                        
    return (cnt**2)

for i in range(n):
    for j in range(m):
        if soldiers[j][i] =="W" and not visited[j][i]:
            W_cnt += wPower(i,j)
            
        elif  soldiers[j][i] == "B" and not visited[j][i]:
            B_cnt += BPower(i,j)
            
print(W_cnt, B_cnt)

            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
