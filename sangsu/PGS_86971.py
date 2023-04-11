# def solution(n, wires):
    
#     graph = [[] for _ in range(n + 1)]
#     for wire in wires:
#         a, b = wire[0], wire[1]
#         graph[a].append(b)
#         graph[b].append(a)
        
#     global count
#     def dfs(V):
#         global count
#         visited[V] = True  # 해당 V값 방문처리)
#         for e in graph[V]:
#             if not visited[e]:
#                 count += 1
#                 dfs(e)
    
#     answer = n+1
#     for wire in wires:
#         visited = [False] * (n + 1)
#         count = 1
#         a, b = wire[0], wire[1]
      
#         graph[a].remove(b)
#         dfs(a)
        
#         answer = min(answer, abs(n-2*count))
#         graph[a].append(b)
#     return answer

def solution(n, wires):
    answer = 1000; idx = -1
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n  + 1)
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    # wires 중 하나의 선 끊기
    for i in range(len(wires)):
        graph[wires[i][0]].remove(wires[i][1])
        # 연결 노드의 개수 체크
        if not visited[wires[i][0]]:
            m = dfs(graph, visited, wires[i][0], 1)
            answer = min(answer, abs((n - m) - m))
        # 두 노드 개수의 차이의 min값 구하기
        graph[wires[i][0]].append(wires[i][1])
    return answer
def dfs(graph, visited, v, cnt):
    visited[v] = True
    for path in graph[v]:
        if not visited[path]:
            dfs(graph, visited, path, cnt+1)
    return cnt
print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))