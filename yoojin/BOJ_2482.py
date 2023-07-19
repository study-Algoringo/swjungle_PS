import sys
read = sys.stdin.readline

n = int(read())
k = int(read())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n+1):
    dp[i][0] = 1
    dp[i][1] = i

for i in range(2, n+1):
    for j in range(2, k+1):
        dp[i][j] = (dp[i-2][j-1] + dp[i-1][j]) % 1000000003

answer = (dp[n-3][k-1] + dp[n-1][k]) % 1000000003
print(answer)