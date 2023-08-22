import sys
read = sys.stdin.readline

n = int(read())
sequence = list(map(int, read().split()))
dp = [1] * (n)

# dp[n] = n번째 원소까지의 수열 중 가장 긴 감소하는 부분수열
# 나보다 큰 수가 나올 때까지 탐색, 해당 인덱스의 dp값에 1 더한 값 vs dp[n] 비교 큰 값을 dp[n]에 저장
for i in range(n):
    for j in range(i):
        if sequence[i] < sequence[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))