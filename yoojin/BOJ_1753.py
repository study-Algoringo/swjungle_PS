import sys
import heapq
read = sys.stdin.readline

v, e = map(int, read().split())
start = int(read())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    u, v, w = map(int, read().split())
    graph[u].append((v, w))

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('INF')] * n
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances

distances = dijkstra(graph, start)
print("\n".join(map(str, distances[1:])))