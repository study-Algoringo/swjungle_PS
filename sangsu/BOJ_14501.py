import sys
input = sys.stdin.readline

n = int(input())
sangdam = []

for i in range(n):
    a,b = map(int, input().split())
    sangdam.append((a,b))
    
dp = [0] * (n+1)

for i in range(n-1, -1,-1):
    if i+sangdam[i][0]>n:
        dp[i] = dp[i+1]
        
    else:
        dp[i] = max(dp[i+1], dp[i+sangdam[i][0]]+ sangdam[i][1] )
        
print(dp[0]) 
    