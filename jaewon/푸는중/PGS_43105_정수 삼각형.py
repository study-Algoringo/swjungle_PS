def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [[0] * (i+1) for i in range(n)]
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i+1):
            # 양끝
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            # 가운데
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    answer = max(dp[n-1])
    return answer

arr = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

# 30
print(solution(arr))

# dp = [
#     [7],
#     [10, 15],
#     [18, 16, 15],
#     [20, 25, 20, 19],
#     [24, 30, 27, 26, 24]
# ]

# triangle = [
#      [7],
#     [3, 8],
#    [8, 1, 0],
#   [2, 7, 4, 4],
#  [4, 5, 2, 6, 5]
# ]