def solution(triangle):
    answer = 0
    dp = []
    for i in triangle:
        lst = []
        for j in i:
            lst.append(0)
        dp.append(lst)

    dp[0][0] = triangle[0][0]
    
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])-1):
            dp[i][j] = max(dp[i][j],dp[i-1][j] + triangle[i][j])
            dp[i][j+1] = dp[i-1][j] + triangle[i][j+1]
    return max(dp[-1])
