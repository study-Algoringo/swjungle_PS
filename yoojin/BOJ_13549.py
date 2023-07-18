import sys
import heapq
read = sys.stdin.readline

# n에서 k로 가는 거리의 최소 값 구하기 (dijkstra)
def dijkstra(start, end):
    dist = [float('inf')] * 100001
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        time, cur = heapq.heappop(pq)

        if cur == end:
            return dist[cur]
        
        if cur * 2 <= 100000 and dist[cur * 2] > dist[cur]:
            dist[cur * 2] = dist[cur]
            heapq.heappush(pq, (dist[cur * 2], cur * 2))
        
        if cur - 1 >= 0 and dist[cur - 1] > dist[cur] + 1:
            dist[cur - 1] = dist[cur] + 1
            heapq.heappush(pq, (dist[cur - 1], cur - 1))

        if cur + 1  <= 100000 and dist[cur + 1] > dist[cur] + 1:
            dist[cur + 1] = dist[cur] + 1
            heapq.heappush(pq, (dist[cur + 1], cur + 1))

    return dist[end]

start, end = map(int, read().split())
result = dijkstra(start, end)
print(result)