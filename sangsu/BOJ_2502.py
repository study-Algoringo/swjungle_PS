//풀이 성공//
import sys
input = sys.stdin.readline

d,k = map(int, input().split())


for i in range(k//2, k):
    dp = [0] * (d+1)
    dp[1] = k
    dp[2] = i
    for j in range(3, d+1):
        if dp[j-2] - dp[j-1] > dp[j-1]:
            break
        
        dp[j] = dp[j-2] - dp[j-1]
        
    if dp[d]:
        print(dp[d], sep='\n')
        print(dp[d-1])
        break
