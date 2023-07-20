import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))

dp = [[0] * (n + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[-i] == arr[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(n - dp[n][n])