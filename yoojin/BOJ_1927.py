import sys
import heapq
read = sys.stdin.readline

n = int(read())
heap = []

for _ in range(n):
    input = int(read())
    if input == 0:
        if len(heap) == 0:
            print(0)
        else:
            e = heapq.heappop(heap)
            print(e)
    else:
        heapq.heappush(heap, input)