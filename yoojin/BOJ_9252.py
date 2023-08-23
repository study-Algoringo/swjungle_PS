import sys
read = sys.stdin.readline

a = [""] + list(read().rstrip())
b = [""] + list(read().rstrip())

answer = []
dp = [[""] * (len(a)) for _ in range(len(b))]
for i in range(1, len(b)):
    for j in range(1, len(a)):
        if b[i] == a[j]:
            # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + 1
            dp[i][j] = dp[i - 1][j - 1] + a[j]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
result = dp[-1][-1]
print(len(result))
print(result)