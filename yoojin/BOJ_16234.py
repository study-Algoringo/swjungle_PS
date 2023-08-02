import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, l, r = map(int, read().split())
graph = []
visited = [[0] * (n + 1) for _ in range(n + 1)]
answer = 0

for _ in range(n):
    graph.append(list(map(int, read().split())))

def dfs(x, y, arr):
    # 방문 표시
    visited[x][y] = 1
    arr.append((x, y))
    sum = graph[x][y]

    for i in range(4):
        # 다음 이동 좌표 구하기
        nx = x + dx[i]
        ny = y + dy[i]
        # 그래프 내에 있고, 방문하지 않은 좌표인 경우
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            # 연합 만드는 조건만족
            if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                sum += dfs(nx, ny, arr)[0]
    return (sum, arr)

def component_sum():
    global visited, answer
    
    # 모든 그래프를 탐색하면서 만약 아직 방문하지 않은 정점을 하나라도 찾으면 dfs
    while True:
        moved = False
        visited = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    sum, arr = dfs(i, j, [])
                    if len(arr) > 1:
                        mean = sum // len(arr)
                        for x, y in arr:
                            graph[x][y] = mean
                        moved = True
    
        if not moved:
            break
        answer += 1

component_sum()
print(answer)