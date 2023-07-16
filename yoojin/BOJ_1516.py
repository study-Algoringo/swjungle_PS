import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
queue = deque([])
dependency = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
time_list = [0 for _ in range(n + 1)]
ret = [0 for _ in range(n + 1)]

for i in range(n):
    line = list(map(int, read().split()))
    time, buildings = line[0], line[1:-1]
    time_list[i+1] = time
    # 종속성이 없는 경우, queue에 넣기
    if not buildings:
        queue.append(i + 1)
    # else, 종속성 배열에 추가
    else:    
        for building in buildings:
            dependency[i+1].append(building)

# queue가 빌 때까지
while queue:
    idx = queue.popleft()
    visited[idx] = True
    ret[idx] += time_list[idx]
    # 종속성 제거
    for i in range(1, n+1):
        if idx in dependency[i]:
            dependency[i].remove(idx)
            ret[i] = max(ret[i], ret[idx])
    # 제거 후 방문하지 않은, 종속성이 빈 애가 생기면 queue에 넣기
    for j in range(1, n+1):
        if not visited[j] and not j in queue and not dependency[j]:
            queue.append(j)

print('\n'.join(map(str, ret[1:])))