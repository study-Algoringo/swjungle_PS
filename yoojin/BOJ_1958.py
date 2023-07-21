import sys
read = sys.stdin.readline

arr = []; answer = 0

for _ in range(3):
    arr.append(read().rstrip())

def solution(str_a, str_b, str_c):
    dp = [[[0] * (len(str_c) + 1) for _ in range(len(str_b) + 1)] for _ in range(len(str_a) + 1)]
    for i in range(1, len(str_a) + 1):
        for j in range(1, len(str_b) + 1):
            for k in range(1, len(str_c) + 1):
                if str_a[i-1] == str_b[j-1] == str_c[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
    return dp[len(str_a)][len(str_b)][len(str_c)]

answer = solution(arr[0], arr[1], arr[2])
print(answer)