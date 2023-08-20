from collections import deque

visited = []

def solution(n, computers):
    global visited
    visited = [0] * (n + 1)
    
    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(i, computers)
            answer += 1
    return answer

def bfs(node, computers):
    n = len(computers)
    queue = deque([node])
    visited[node] = 1
    
    # bfs 이용해 connected component 개수 구하기
    while queue:
        cur_node = queue.popleft()
        for i in range(n):
            if not visited[i] and computers[cur_node][i] == 1 and cur_node != i:
                queue.append(i)
                visited[i] = 1