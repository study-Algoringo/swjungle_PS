def solution(n):
    # 피보나치
    d = [0] * 60000
    answer = 0
    d[1] = 1
    d[2] = 2
    for i in range(3, n + 1):
        d[i] = (d[i -1] + d[i - 2]) %  1000000007
        answer += d[n]
    return answer
