# 최단경로 1753
# 출발 노드 설정
# 최단 거리 테이블을 1e9로 초기화
# 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
# 해당 노드를 거쳐 다른 노드로 가는 비용을 계산, 테이블 갱신
# 3, 4번 반복
import heapq
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())
graph = [[] * (n + 1) for _ in range(n+1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
