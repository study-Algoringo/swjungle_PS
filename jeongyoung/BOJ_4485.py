import heapq as hq

# 입력 케이스 여러 개 = while문
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 1

while True:
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)] # 동굴 정보
    # 돈으로 방문 체크해야함
    visited = [[False] * n for _ in range(n)]
    heap = list()
    visited[0][0] = True
    # 시작 노드, 잃는 소지금이 적을수록 우선순위 높음
    hq.heappush(heap, (cave[0][0], 0, 0))
    while heap:
        cost, rx, ry = hq.heappop(heap)
        if rx == n - 1 and ry == n - 1:
            print("Problem %d: %d" % (cnt, cost))
            break
        for i in range(4):
            x = rx + dx[i]
            y = ry + dy[i]
            if 0 <= x < n and 0 <= y < n and visited[x][y] == 0:
                visited[x][y] = 1
                hq.heappush(heap, (cost + cave[x][y], x, y))
    cnt += 1
    
    
