import heapq
def solution(scoville, K):
    answer = 0
    result = scoville
    heapq.heapify(result)
    
    while result[0] < K:
        if len(result) == 1:
            return -1
        answer+=1  
        heapq.heappush(result,heapq.heappop(result) + heapq.heappop(result) * 2)
    return answer

print(solution([1,2,3,9,10,12],7))