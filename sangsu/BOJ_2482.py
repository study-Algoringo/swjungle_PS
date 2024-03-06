import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

dp = [[[],[]] for _ in range(n+1)]

dp[1][0].append(1)
dp[1][1].append(0)

for i in range(2, n+1):
    for j in dp[i-1][0]:
        dp[i][1].append(j)
        
    for p in dp[i-1][1]:
        dp[i][1].append(p)
        dp[i][0].append(p+1)
        
x = dp[n][0].count(k)
y = dp[n][1].count(k)

answer = x//2+ y
print(answer)


