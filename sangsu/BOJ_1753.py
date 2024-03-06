import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
k = int(input())
distance = [INF]*(n+1)
for i in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(start):
    node = []
    heapq.heappush(node, (0,start))
    distance[start] = 0
    while node:
        dist, now = heapq.heappop(node)
        if distance[now] < dist:
            continue
        for temp in graph[now]:
            cost = dist + temp[1]
            if cost < distance[temp[0]]:
                distance[temp[0]] = cost
                heapq.heappush(node, (cost, temp[0]))

dijkstra(k)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
    

    
