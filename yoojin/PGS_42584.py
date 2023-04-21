def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        second = 0
        for j in range(i+1, len(prices)):
            second += 1
            if prices[i] > prices[j]:
                break
        answer.append(second)
    answer.append(0)
    
    return answer