# [BOJ] 색상환 / Gold 3 / 2482 / 박정영

# 인접한 색은 동시에 사용 안함
# 직선으로 생각 -> 인접한 색을 제외하고 뽑는 경우의 수
# 원형으로 생각 -> 인접한 색이 2개
n = int(input())
k = int(input())
mod = 1000000003

dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 1
    dp[i][1] = i
    
for i in range(2, n + 1):
    for j in range(2, k + 1):
        if i == n:
            dp[i][j] = dp[i - 3][j - 1] + dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 2][j - 1] + dp[i - 1][j]
        dp[i][j] %= mod
print(dp[n][k])
