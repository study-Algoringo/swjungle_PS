import sys
from collections import deque
read = sys.stdin.readline

answer = 0
n, m = map(int, read().split())
connections = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, read().split())
    connections[a].append(b)
    connections[b].append(a)

# 경로의 길이가 연결된 노드의 수보다 1 작고, 노드의 개수가 5보다 큰 경우 return True
def dfs(node, depth, visited):
    global answer
    visited[node] = 1

    if depth == 4:
        answer = 1
        return

    # 현재 노드에서 갈 수 있으면 go
    for i in connections[node]:
        if not visited[i]:
            dfs(i, depth + 1, visited)
            visited[i] = 0

for i in range(n):
    dfs(i, 0, [0] * (n + 1))
    if answer:
        break

if answer:
    print(1)
else:
    print(0)