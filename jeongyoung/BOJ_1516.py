# 게임 개발 1516
from collections import deque

n = int(input()) # 건물의 수
# 건물을 짓는데 걸리는 시간, 그 건물을 짓기 위해 먼저 지어야하는 번호
building = [[] for i in range(n + 1)]
# 진입 차수
indegree = [0] * (n + 1)
# 건물 짓기 위해 걸리는 시간
cost = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))[:-1]
    cost[i] = data[0]
    building_data = data[1:]
    # 진입차수 설정
    for j in building_data:
      building[j].append(i)
      indegree[i] += 1

# 위상정렬 절차
# 진입차수가 0인 노드를 큐에 삽입한다
# 큐가 빌때까지 큐에서 원소를 꺼내고,
# 꺼낼때 그래프에서 진입 차수가 0인 노드를 새로 큐에 삽입
def topology_sort():
    result = [0] * (n + 1)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # 큐에서 꺼낸 건물의 시간을 저장
        # 앞선 건물 짓는데 걸리는 시간 + 현재 걸리는 시간을 저장
        result[now] += cost[now]
        for a in building[now]:
            indegree[a] -= 1
            # 시간 갱신
            result[a] = max(result[a], result[now])
            if indegree[a] == 0:
                q.append(a)
    return result

answer = topology_sort()
for i in range(1, n + 1):
    print(answer[i])
