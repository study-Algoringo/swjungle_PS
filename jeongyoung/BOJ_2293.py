# 동전 1 2293
n, k = map(int, input().split())
coin = [int(input()) for i in range(n)] # 동전 종류
dp = [0 for i in range(k + 1)]
dp[0] = 1

for i in coin:
    for j in range(i, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[k])
