# 정렬로 풀이
# import sys
# N = int(sys.stdin.readline())
# result = []
# for i in range(N):
#     result.extend(map(int,sys.stdin.readline().split()))
#     if len(result) > N:
#         result.sort(reverse=True)
#         result = result[:N]
# print(result[-1])

# 우선순위 큐로 풀이
import heapq
heap = []
n = int(input())

for _ in range(n):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap) < n: # heap의 크기를 n개로 유지
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])

