import sys
import math
import heapq
read = sys.stdin.readline

t = int(read())

def solution():
    areas = []
    n, k = map(int, read().split())
    for i in range(n):
        r, h = map(int, read().split())
        areas.append((r, h))
    areas.sort()
    
    result, min_heap = 0, []
    for area in areas:
        if len(min_heap) == k - 1:
            result = max(result, area[0] * area[0] + 2 * area[0] * area[1] + sum(min_heap))
        heapq.heappush(min_heap, 2 * area[0] * area[1])
        if len(min_heap) >= k:
            heapq.heappop(min_heap)
    return result * math.pi
    
for case in range(t):
    print("Case #%d: %s" % (case + 1, solution()))


# 넓이 => 가장 밑에 깔린 펜케이크의 bottom area + (n개의 side area 합)
## 1위~n위까지의 side area 합 + 그중 가장 넓은 bottom area
## 2위~n위까지의 side area 합 + 가장 넓은 bottom area
## 두 넓이 중 큰 넓이를 ans로
