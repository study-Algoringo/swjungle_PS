def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        DP = [1,2] + [0]*(n-2)
        for i in range(3,n+1):
            DP[i-1] = (DP[i-2] + DP[i-3])%1000000007 # key-point
        return DP[n-1]