def solution(n):
    DP = [1,2] + [0]*(n-2)
    for i in range(3,n+1):
        DP[i-1] = (DP[i-2] + DP[i-3])%1000000007 # key-point
    return DP[n-1]

    