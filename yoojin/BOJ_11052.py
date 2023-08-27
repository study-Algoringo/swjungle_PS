import sys
read = sys.stdin.readline

n = int(read())
cards = [0] + list(map(int, read().split()))
dp = [0] * (n + 1)
dp[1] = cards[1]

# dp[n] -> 카드 n개를 가지기 위해 지불해야 하는 최댓값
# dp[n] = max(dp[n - 1] + cards[1], dp[n - 2] + cards[2], ..., dp[1] + cards[n-1])
for i in range(1, n + 1):
    dp[i] = cards[i]
    for j in range(i):
        dp[i] = max(dp[i], dp[i - j] + dp[j])
print(dp[n])