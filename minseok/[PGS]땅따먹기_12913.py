def solution(land):
    maxn = 0
    dp = [land[0]]
    for _ in range(len(land)-1):
        dp.append([0,0,0,0])

    for i in range(1,len(land)):
        for j in range(4):
            dp[i][j] = max(dp[i-1][:j] + dp[i-1][j+1:]) + land[i][j]

    return max(dp[-1])