from collections import deque

def stay(start, maps):
    island = deque([start])
    cnt = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while island:
        x,y = island.popleft()
        if maps[x][y] != 'X':
            cnt += int(maps[x][y])
            maps[x][y] = 'X'
            for i in range(4):
                nx = x +dx[i]
                ny = y +dy[i]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X':
                    island.append((nx, ny))
        
        
    return cnt
                        
def solution(maps):
    m = len(maps)
    n = len(maps[0])
    answer = []
    for i in range(m):
        maps[i] = list(maps[i])
    
    for i in range(m):
        for j in range(n):
            if maps[i][j] != 'X':
                answer.append(stay((i,j),maps))
    
    answer.sort()
   
        
        
    return answer if answer else [-1]


print(solution(["X591X","X1X5X","X231X", "1XXX1"]))