import sys
read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))

# dp[i][j] => i번까지의 연속 합, j는 제외 여부
dp = [[0] * 2 for _ in range(n)]
dp[0][0] = nums[0]; dp[0][1] = 0

ans = -1e9
if n > 1:
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0] + nums[i], nums[i])
        dp[i][1] = max(dp[i-1][0], dp[i-1][1] + nums[i])
        ans = max(ans, dp[i][0], dp[i][1])
else:
    ans = nums[0]

print(ans)