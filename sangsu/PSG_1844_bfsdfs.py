from collections import deque
def solution(maps):
    answer = 0
    m = len(maps)
    n = len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    que = deque()
    que.append([0,0])
    while que:
        location = que.popleft()
        x,y = location[0], location[1]
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if nx>=0 and nx<m and ny>=0 and ny<n and maps[nx][ny] != 0:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    que.append([nx, ny])
    if  maps[m-1][n-1] == 1:
        answer = -1             
    else:
        answer = maps[m-1][n-1]
    
    
    return answer