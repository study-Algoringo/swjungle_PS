def solution(n):
    answer = 0
    m = 1
    while bin(n).count('1') != bin(n+m).count('1'):
        m += 1
    answer = n+m
    return answer
