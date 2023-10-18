import sys
read = sys.stdin.readline

n = int(read())
house = []; dp = [[0] * 3 for _ in range(n)]

for _ in range(n):
    house.append(list(map(int, read().split())))

# n번째 최소 비용 -> n - 1번째 최소 비용 + n번째 집에 칠할 수 있는 색 중 최소 값
dp[0] = house[0]
for i in range(1, n):
    for j in range(3):
        dp[i][j] = house[i][j] + min(dp[i-1][(j + 1) % 3], dp[i-1][(j + 2) % 3])

print(min(dp[n-1]))