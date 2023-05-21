def solution(land):
    answer = 0
    dp = [[0,0,0,0] for _ in range(len(land))]
    dp[0] = land[0]

    # 행 계산
    for i in range(1,len(land)):
        # 열 계산
        for j in range(4):
            if j == 0:
                dp[i][j] = max(dp[i-1][1],dp[i-1][2],dp[i-1][3])
            elif j == 1:
                dp[i][j] = max(dp[i-1][0],dp[i-1][2],dp[i-1][3])
            elif j == 2:
                dp[i][j] = max(dp[i-1][0],dp[i-1][1],dp[i-1][3])
            else:
                dp[i][j] = max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
            dp[i][j] += land[i][j]

    return max(dp[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))