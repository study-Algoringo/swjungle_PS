import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    indegree[b] += 1

# indegree가 0인 것부터 queue에 추가
queue = deque([]); ret = [1 for _ in range(n+1)]
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    curr = queue.popleft()
    for i in graph[curr]:
        indegree[i] -= 1
        ret[i] = ret[curr] + 1
        # indegree가 0인 원소 있으면 queue에 추가
        if indegree[i] == 0:
            queue.append(i)

print(' '.join(map(str, ret[1:])))