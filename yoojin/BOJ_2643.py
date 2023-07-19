import sys
read = sys.stdin.readline

n = int(read())
papers = []; dp = [1 for _ in range(n)]

for _ in range(n):
    a, b = map(int, read().split())
    papers.append(sorted((a, b), reverse=True))

papers.sort(reverse=True)
# 현재 색종이를 쌓을 수 있는 경우, dp 배열 업데이트
for i in range(1, n):
    for j in range(i):
        if papers[i][1] <= papers[j][1]:
            # dp[n] = n번째까지의 최대 색종이 장수
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))