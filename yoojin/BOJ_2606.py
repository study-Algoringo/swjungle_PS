import sys
read = sys.stdin.readline

cnt = 0
def dfs(graph, start, visited):
    global cnt
    visited[start] = True
    cnt += 1
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

v = int(read())
e = int(read())

visited = [0] * (v + 1)
graph = [[] for i in range(v+1)]
for _ in range(e):
    num_1, num_2 = map(int, read().split())
    graph[num_1].append(num_2)
    graph[num_2].append(num_1)

dfs(graph, 1, visited)
print(cnt - 1)