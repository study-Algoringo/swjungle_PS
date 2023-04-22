from collections import deque

def solution(scoville, K):
    scoville.sort()
    que = deque(scoville)
    cnt = 0            

    while que:
        n = que.popleft()
        m = que.popleft()
        cal = n + 2 * m
        cnt += 1
        
        que.appendleft(cal)
        
        if min(que) >= K:
            break

    answer = cnt
    return answer

solution([1, 2, 3, 9, 10, 12], 7)