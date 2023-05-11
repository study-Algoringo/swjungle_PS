def solution(k, tangerine):
    answer = 0
    count = [0] * 100000
    for tan in tangerine:
        count[tan] += 1
        
    while k > 0:
        mx = max(count)
        if mx == 0:
            return 0
        k = k - mx
        count[count.index(mx)] = 0
        answer += 1

    return answer