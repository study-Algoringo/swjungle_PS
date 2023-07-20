import sys
read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))

dp = [1 for _ in range(n)]
# dp[n] -> n번째까지 넣을 수 있는 상자의 최대값

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))