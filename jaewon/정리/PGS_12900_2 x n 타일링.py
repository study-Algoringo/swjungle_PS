# def fibo(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     return fibo(n-1) + fibo(n-2) % 1000000007

def solution(n):
    answer = 0;
    dp = [0] * 60001
    dp[1] = 1
    dp[2] = 2

    for i in range(3, 60001):
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007

    answer = dp[n]    
    return answer

print(solution(10))