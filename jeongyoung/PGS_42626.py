import heapq
def solution(s, k):
    heap = []
    for i in s:
        heapq.heappush(heap, i)
    cnt = 0
    while heap[0] < k:
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        cnt += 1
        
        if len(heap) == 1 and heap[0] < k:
            return -1
    return cnt
# def solution(scoville, K):
#     s = sorted(scoville)
#     cnt = 0
#     for i in s:
#         if i < K: 
#             s.append(s[0] + s[1]*2)
#             s.sort()
#             s = s[2:]
#             cnt += 1
#         if s[0] > K:
#             break
#         if(len(s) == 1) and s[0] < K:
#             return -1
#     return cnt
