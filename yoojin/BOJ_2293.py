import sys
read = sys.stdin.readline

n, k = map(int, read().split())
coins = []
dp = [0] * (k + 1)

for _ in range(n):
    coins.append(int(read()))

dp[0] = 1
for coin in coins:
    for i in range(coin, k  + 1):
        dp[i] += dp[i - coin]
print(dp[k])