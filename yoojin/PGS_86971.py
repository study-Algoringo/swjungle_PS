def solution(n, wires):
    answer = 1000
    graph = [[] for _ in range(n + 1)]
    
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    
    for i in range(len(wires)):
        visited = [0] * (n  + 1)
        # wires 중 하나의 선 끊기
        graph[wires[i][0]].remove(wires[i][1])
        # 연결 노드의 개수 체크
        m = dfs(graph, visited, wires[i][0], 0)
        # 두 노드 개수의 차이의 min값 구하기
        answer = min(answer, abs((n - m) - m))
        # 선 다시 이어주기
        graph[wires[i][0]].append(wires[i][1])

    return answer

def dfs(graph, visited, v, cnt):
    visited[v] = True
    cnt = cnt + 1
    for path in graph[v]:
        if not visited[path]:
            cnt = dfs(graph, visited, path, cnt)
    return cnt