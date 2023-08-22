import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

n = int(read())
edges = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b, cost = map(int, read().split())
    edges[a].append((b, cost))
    edges[b].append((a, cost))

# 한 점으로부터 시작하여 갈림길이 있을 때마다 큰 가중치 노드로 이동
# 더이상 갈 수 없으면 종료

def dfs(node, wei):
    for i in edges[node]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)

distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))