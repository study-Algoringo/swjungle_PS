import sys
from collections import deque
sys.stdin=open("/Users/admin/Documents/swjungle_PS/jaewon/푸는중/input.txt", "rt")
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j, graph, costs):
    queue = deque()
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if costs[nx][ny] > costs[x][y] + graph[nx][ny]:
                    costs[nx][ny] = costs[x][y] + graph[nx][ny]
                    queue.append((nx, ny))

count = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    costs = [[int(1e9)] * n for _ in range(n)]
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    costs[0][0] = graph[0][0]
    bfs(0, 0, graph, costs)
    print(f"Problem {count}: {costs[n-1][n-1]}")
    count += 1










# Problem 1: 20
# Problem 2: 19
# Problem 3: 36