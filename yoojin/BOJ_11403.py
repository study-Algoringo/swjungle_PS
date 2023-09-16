import sys
read = sys.stdin.readline

n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]
visited = [0 for _ in range(n)]

# 시작점 i에서 시작했을 때, 도착할 수 있는 지점을 모두 표시함 (i, j)
def dfs(node):
    # 갈 수 있는 모든 정점을 dfs로 탐색
    for i in range(n):
        if graph[node][i] == 1 and not visited[i]:
            visited[i] = 1
            dfs(i)

for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [0 for _ in range(n)]
