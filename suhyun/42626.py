import heapq
def solution(scoville, K):
    answer = 0
    result = scoville
    length = len(scoville)
    heapq.heapify(result)
    
    while result[0] < K:
        if len(result) == 1:
            return -1
        
        answer+=1  
        temp = heapq.heappop(result) + heapq.heappop(result) * 2
        heapq.heappush(result,temp)

    return answer

print(solution([0,0,0,0,0],7))