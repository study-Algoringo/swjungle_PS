import sys
read = sys.stdin.readline

n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]

# 시작점 i에서 시작했을 때, 도착할 수 있는 지점을 모두 표시함 (i, j)
def dfs(node, visited):
    visited[node] = True
    # 갈 수 있는 모든 정점을 dfs로 탐색
    for i in graph[node]:
        if i == 1:
            dfs(i, visited)