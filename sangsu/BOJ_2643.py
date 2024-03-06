import sys
input = sys.stdin.readline

n = int(input())
papers = []
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        papers.append([a,b])
    else:
        papers.append([b,a])
        
        
papers.sort(reverse = True)

dp = [[[0,0,0], [0,0,0]] for _ in range(n)]

dp[0][0][0], dp[0][0][1], dp[0][0][2] = papers[0][0], papers[0][1], 1
dp[0][1][0], dp[0][1][1], dp[0][1][2] = 1000, 1000, 0

for i in range(1, n):
    x_1, y_1, z_1 = dp[i-1][0][0], dp[i-1][0][1], dp[i-1][0][2]
    x_2, y_2, z_2 = dp[i-1][1][0], dp[i-1][1][1], dp[i-1][1][2]
    if x_1 >= papers[i][0] and y_1 >= papers[i][1]:
        dp[i][0][0],  dp[i][0][1],  dp[i][0][2] = papers[i][0], papers[i][1], z_1+1
        
    else:
        if  x_2 >= papers[i][0] and y_2 >= papers[i][1]:
            dp[i][0][0],  dp[i][0][1],  dp[i][0][2] = papers[i][0], papers[i][1], z_2+1
            
        else:
             dp[i][0][0],  dp[i][0][1],  dp[i][0][2] = x_1, y_1, z_1
             
    dp[i][1][0],  dp[i][1][1],  dp[i][1][2] = x_1, y_1, z_1
    
print(max(dp[n-1][0][2], dp[n-1][1][2]))