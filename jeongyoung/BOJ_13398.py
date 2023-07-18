import sys
input = sys.stdin.readline

N = int(input())
input_array = list(map(int, input().split()))
dp = [[x for x in input_array] for _ in range(2)]

for i in range(1, N):
    dp[0][i] = max(dp[0][i - 1] + input_array[i], dp[0][i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + input_array[i])

print(max(max(dp[0]), max(dp[1])))
