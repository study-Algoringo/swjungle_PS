from collections import deque
def solution(prices):
    answer = []
    
    que = deque(prices)

    while que:
        w = que.popleft()
        cnt=0
        for data in que:
            cnt+=1
            if w > data:
                break

        answer.append(cnt)

    return answer

print(solution([1, 2, 3, 2, 3]))