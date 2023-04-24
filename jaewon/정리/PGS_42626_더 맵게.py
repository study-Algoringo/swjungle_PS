import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        # 가장 작은 수와 다음으로 작은 수 뽑기
        smallest_val = heapq.heappop(scoville)
        second_smallest_val = heapq.heappop(scoville)
        # 가장 작은 수가 K보다 크다면 return
        if smallest_val >= K:
            return answer

        # 새로운 음식을 만든 후, 스코빌 지수 업데이트
        new_val = smallest_val + (second_smallest_val * 2)
        heapq.heappush(scoville, new_val)
        answer += 1

    if heapq.heappop(scoville) < K:
        return -1
    else:
        return answer

print(solution([6,2],7))