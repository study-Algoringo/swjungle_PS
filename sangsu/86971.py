def solution(n, wires):
    
    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        a, b = wire[0], wire[1]
        graph[a].append(b)
        graph[b].append(a)
        
    global count
    def dfs(V):
        global count
        visited[V] = True  # 해당 V값 방문처리)
        for e in graph[V]:
            if not visited[e]:
                count += 1
                dfs(e)
    
    answer = n+1
    for wire in wires:
        visited = [False] * (n + 1)
        count = 1
        a, b = wire[0], wire[1]
      
        graph[a].remove(b)
        dfs(a)
        
        answer = min(answer, abs(n-2*count))
        graph[a].append(b)
    return answer