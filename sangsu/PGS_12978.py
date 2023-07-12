import heapq
def solution(N, road, K):
    answer = 0
    min_time = [int(1e9)] * (N+1)
    graph = [[] for _ in range(N+1)]
    for rd in road:
        a,b,c = rd[0], rd[1], rd[2]
        graph[a].append([b,c])
        graph[b].append([a,c])
    
    q = []
    heapq.heappush(q, (0, 1))
    min_time[1] = 0
    while q:
        time, now = heapq.heappop(q)
        if min_time[now]< time:
            continue
        
        for info in graph[now]:
            cost = time + info[1]
            if cost < min_time[info[0]]:
                min_time[info[0]] = cost
                heapq.heappush(q, (cost, info[0]))
    for i in min_time:
        if i <= K:
            answer+= 1        
        
    return answer

print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))