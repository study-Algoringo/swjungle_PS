def solution(n):
    dp = [0]*60001
    dp[1],dp[2]=1,2

    if n == 1:
        return 1
    if n == 2:
        return 2
    for i in range(3,n+1):
        dp[i] = (dp[i-2]+dp[i-1])%1000000007
        
    return dp[n]
