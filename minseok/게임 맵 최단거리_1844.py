from collections import deque

def solution(maps):
    visit = [[0]*len(maps[0]) for _ in range(len(maps))]  # 방문처리할 visit 리스트 생성
    visit[0][0] = 1                                       # vist 시작점은 1
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque([(0,0)])

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if len(maps) > nx >= 0 and len(maps[0]) > ny >= 0:
                if maps[nx][ny] == 1 and visit[nx][ny] == 0:    # 다음 노드가 이동 가능한 길이면서 방문하지 않았을때
                    visit[nx][ny] = visit[x][y] + 1             # 이전 노드의 값에 1을 더해주면서 방문처리
                    q.append((nx,ny))                           # 방문한 위치 저장
                    
    if visit[-1][-1] == 0:      # 도착점이 0일 경우 도달할 방법이 없으므로 -1 출력
        return -1
    else:   
        return visit[-1][-1]
