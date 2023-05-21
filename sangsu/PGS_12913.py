def solution(land):
    answer = 0
    l = len(land)
    dp = [[0,0,0,0] for _ in range(l)]
    dp[0] = land[0]
    for i in range(1, l):
        dp[i][0] = max(dp[i-1][1] + land[i][0], dp[i-1][2] + land[i][0], dp[i-1][3] + land[i][0])
        dp[i][1] = max(dp[i-1][0] + land[i][1], dp[i-1][2] + land[i][1], dp[i-1][3] + land[i][1])
        dp[i][2] = max(dp[i-1][0] + land[i][2], dp[i-1][1] + land[i][2], dp[i-1][3] + land[i][2])
        dp[i][3] = max(dp[i-1][0] + land[i][3], dp[i-1][1] + land[i][3], dp[i-1][2] + land[i][3])
    answer = max(dp[l-1])

    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))