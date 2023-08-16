import sys
from itertools import combinations
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [[] for _ in range(n + 1)]
nums = [i for i in range(1, n + 1)]

for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

# combination으로 노드 2개만 선택해서 계산
def calculate(start, visited, chickens):
    # 선택되지 않은 나머지 n-2개의 점에 대해서 depth * 2를 더하기
    queue = deque([(start, 0)])
    visited[start] = 1

    while queue:
        node, depth = queue.popleft()
        if node in chickens:
            return depth * 2

        for i in graph[node]:
            if not visited[i]:
                queue.append((i, depth + 1))
                visited[i] = 1

answer = 1e9; com = 0
for combi in combinations(nums, 2):
    ret = 0
    for j in range(1, n + 1):
        ret += calculate(j, [0] * (n + 1), combi)

    if answer > ret:
        answer = ret
        com = combi

for i in com:
    print(i, end=' ')
print(answer)