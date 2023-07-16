import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
building_list = [[] for _ in range(n+1)]
cost = [0]*(n+1)
indegree = [0] *(n+1)

for i in range(1,n+1):
    building = list(map(int, input().split()))
    cost[i] = building[0]
    need_building = building[1:-1]
    for need in need_building:
        building_list[need].append(i)
        indegree[i] += 1
        
que = deque([])
result = [0]*(n+1)
for i in range(1,n+1):
    if not indegree[i]:
        que.append(i)
        
while que:
    a = que.popleft()
    result[a] += cost[a]
    for building in building_list[a]:
        result[building] = max(result[building], result[a])
        indegree[building] -= 1
        if indegree[building] == 0:
            que.append(building)
            
for i in range(1, n+1):
    print(result[i])
    