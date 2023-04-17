def solution(prices):
    answer = []
    while prices:
        x = prices.pop(0)
        cnt = 0

        for price in prices:
            if x <= price:
                cnt += 1

        answer.append(cnt)
    return answer

solution([10, 20, 30, 20, 30])