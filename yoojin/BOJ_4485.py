import sys
import heapq
read = sys.stdin.readline

cnt = 0
INF = sys.maxsize
d = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def dijkstra():
    # 값이 최소인 정점 선택 -> 연관된 정점의 최소 거리 구하기
    q = []
    heapq.heappush(q, (cave[0][0], 0, 0))
    dist[0][0] = 0
    # [0, 0]부터 시작하여 인접한 정점에 대해 거리를 더한 값을 현재까지의 최소 거리와 비교하여 갱신
    while q:
        cost, x, y = heapq.heappop(q)

        if x == n-1 and y == n-1:
            print(f'Problem {cnt}: {dist[x][y]}')
            break

        for i in range(4):
            new_x = x + d[i][0]
            new_y = y + d[i][1]

            if 0 <= new_x < n and 0 <= new_y < n:
                new_cost = cost + cave[new_x][new_y]

                if new_cost < dist[new_x][new_y]:
                    dist[new_x][new_y] = new_cost
                    heapq.heappush(q, (new_cost, new_x, new_y))

while True:
    n = int(read())
    if n == 0:
        break
    
    cave = [list(map(int, read().split())) for _ in range(n)]
    dist = [[INF for _ in range(n)] for _ in range(n)]

    dijkstra()
    cnt += 1
