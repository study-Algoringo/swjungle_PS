import sys
read = sys.stdin.readline

n = int(read())
consulting = []
dp = [0] * (n + 1)

for i in range(n):
    t, p = map(int, read().split())
    consulting.append((t, p))

# dp[n]이 n번째 날까지 최대 수익이라고 하면
# n까지 오는 여러 경우의 수 중 최댓값 즉 i + Ti = n을 만족하는 dp[i] + Pi 중 최대
for i in range(n):
    t, p = consulting[i]
    if i + t <= n:
        dp[i + t] = max(dp[i + t], dp[i] + p)
    # 상담을 하지 않는 날도 dp값이 갱신되도록
    dp[i + 1] = max(dp[i + 1], dp[i])
    
print(dp[n])