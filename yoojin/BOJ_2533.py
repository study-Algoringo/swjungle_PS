import sys
sys.setrecursionlimit(10**9)
read = sys.stdin.readline

n = int(read())
graph = [[] for _ in range(n + 1)]
dp = [[0, 0] for _ in range(1000001)]
visited = [False for _ in range(1000001)]

def find(x):
    visited[x] = True
    dp[x][0] = 1
    for i in range(len(graph[x])):
        child = graph[x][i]
        if visited[child]:
            continue
        find(child)
        dp[x][1] += dp[child][0]
        dp[x][0] += min(dp[child][1], dp[child][0])

for _ in range(n - 1):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

find(1)
print(min(dp[1][0], dp[1][1]))