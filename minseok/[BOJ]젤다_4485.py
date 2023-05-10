import sys
input = sys.stdin.readline
import heapq 

def dijkstra(n):
    q = []
    heapq.heappush(q,(0,0,loopy[0][0]))  # 출발지의 비용, 좌표(x,y), 비용(해당 좌표의 루피 값)을 힙에 추가

    move = [[-1,0], [0, -1], [0, 1], [1, 0]]

    visited = [[int(1e9)]*n for _ in range(n)]
    visited[0][0] = loopy[0][0]

    while q:
        x,y,cost = heapq.heappop(q) # 현재 좌표의 비용이 가장 작은 것을 꺼냄
        for i in range(4):
            nx, ny = move[i][0] + x, move[i][1] + y
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            newcost = loopy[nx][ny] + cost  # 새로운 좌표로 이동했을 때의 루피 값

            if newcost < visited[nx][ny]:   # 새로운 좌표의 루피 값이 현재까지 저장된 루피 값보다 작으면 갱신
                visited[nx][ny] = newcost
                heapq.heappush(q,(nx,ny,newcost))   # 우선순위 큐에 해당 좌표와 루피 값 추가
    return visited

cnt = 1
while True:
    n = int(input())

    if n == 0 :
        break

    loopy = [list(map(int,input().split())) for _ in range(n)]
    
    ans = dijkstra(n)
    print(f"Problem {cnt}: {ans[n-1][n-1]}")
    cnt += 1