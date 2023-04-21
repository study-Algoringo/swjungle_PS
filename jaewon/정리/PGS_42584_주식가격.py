from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        cnt = 0
        x = prices.popleft()

        for price in prices:
            cnt += 1
            if x > price:
                break
        answer.append(cnt)

    return answer

solution([3, 1])