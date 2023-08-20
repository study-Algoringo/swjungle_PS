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
answer = 0

def dfs(node, cost, visited):
    global answer
    visited[node] = 1
    node_list = [edge for edge in edges[node] if not visited[edge[0]]]
    # 현재 노드에서 갈 수 있는 모든 길 중 가중치가 큰 노드 선택하기
    if len(node_list) == 0:
        answer = max(answer, cost)
        return
    
    max_node = max(node_list, key=lambda x: x[1])
    dfs(max_node[0], cost + max_node[1], visited)

for i in range(1, n + 1):
    dfs(i, 0, [0] * (n + 1))
print(answer)