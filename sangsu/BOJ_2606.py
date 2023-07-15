import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
m = int(input())
network = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

virus = deque([1])
visited = [0]*(n+1)
visited[1] = 1
while virus:
    k = virus.popleft()
    for computer in network[k]:
        if not visited[computer]:
            visited[computer] = 1
            virus.append(computer)
            

print(visited.count(1)-1)

