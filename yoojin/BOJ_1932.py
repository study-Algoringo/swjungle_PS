import sys
read = sys.stdin.readline

n = int(read())
triangle = [[] for _ in range(n + 1)]
dp = [[0] * n for _ in range(n)]

for i in range(n):
    triangle[i] = list(map(int, read().split()))

dp[0] = triangle[0]

# 각 줄을 i, 번호를 j(0<=j<=i)라고 하면 dp[i][j] = dp[i-1][j-1], dp[i-1][j](j가 1~i-1)
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][0] = dp[i-1][0] + triangle[i][0]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[n-1]))