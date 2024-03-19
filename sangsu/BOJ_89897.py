def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = []
    for i in range(n):
        dp.append([0]*(i+1))
    
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] +triangle[i][0]
        dp[i][i] = dp[i-1][i-1] +triangle[i][i]
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j-1]+triangle[i][j], dp[i-1][j]+triangle[i][j])
            
    answer = max(dp[n-1])
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))