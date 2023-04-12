from collections import deque

def bfs(start, visitied, graph):
    queue = deque([start])
    result = 1
    visitied[start] = True
    while queue:
        now = queue.popleft()
        # now의 이웃을 반복
        # 인덱스 'i'의 각 요소는 인덱스 'now'가 있는 노드의 모든 이웃 목록이다.
        for i in graph[now]:
            if visitied[i] == False:
                result += 1
                # 방문하지 않은 이웃 i를 추가 -> 이를 통해서 방문하지 않은 노드를 기준으로 다시한번 인접노드를 탐색할수 있다.
                queue.append(i)
                visitied[i] = True
    return result

def solution(n, wires):
    answer = n
    # 전체 연결 정보를 저장
    graph = [[] for _ in range(n+1)]
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    # 검색할 위치, 끊을 위치
    for start, not_visit in wires:
        visitied = [False]*(n+1)
        visitied[not_visit] = True
        result = bfs(start, visitied, graph)
        if abs(result - (n-result)) < answer:
            answer = abs(result - (n-result))
    return answer

wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
# wires = [[1,2],[2,3],[3,4]]
# 송전탑 개수, 전선정보
solution(9, wires)
# solution(4, wires)