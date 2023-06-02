import heapq

def dijkstra(start, graph, distance):
    queue = []
    heapq.heappush(queue, (0, start))  # (거리, 노드)
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] < dist:
            continue

        for n, d in graph[node]:
            cost = dist + d

            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(queue, (cost, n))


def solution(N, road, K):
    # 그래프 초기화
    graph = [[] for _ in range(N+1)]
    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 최단 거리 테이블 초기화
    INF = int(1e9)
    distance = [INF] * (N+1)

    dijkstra(1, graph, distance)  # 1번 노드부터 출발하여 최단 거리 계산

    # 배달 가능한 음식점 개수 세기
    count = 0
    for dist in distance:
        if dist <= K:
            count += 1

    return count
