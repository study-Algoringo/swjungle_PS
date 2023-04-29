import sys
input = sys.stdin.readline
rock = []
n = int(input())
for i in range(n-1):
    a,b = map(int, input().split())
    rock.append([a,b])
    
k = int(input())
dp = [[0,0] for _ in range(n)]
if n == 1:
    print(0)
    exit(0)
elif n == 2:
    print(rock[0][0])
    exit(0)
elif n == 3:
    print(min(rock[0][0]+rock[1][0], rock[0][1]))
    exit(0)
elif n == 4:    
    print(min(k, rock[0][0]+rock[1][0]+rock[2][0], rock[0][1]+rock[2][0], rock[0][0]+rock[1][1]))
    
else:
    dp[0][0],dp[0][1] = 0,0
    dp[1][0],dp[1][1] = rock[0][0],rock[0][0]
    dp[2][0],dp[2][1] = min(rock[0][0]+rock[1][0], rock[0][1]), min(rock[0][0]+rock[1][0], rock[0][1])
    dp[3][0],dp[3][1] = min(rock[0][0]+rock[1][0]+rock[2][0], rock[0][1]+rock[2][0], rock[0][0]+rock[1][1]), min(k, rock[0][0]+rock[1][0]+rock[2][0], rock[0][1]+rock[2][0], rock[0][0]+rock[1][1])
    for i in range(4, n):
        dp[i][0] = min(dp[i-2][0]+rock[i-2][1], dp[i-1][0]+rock[i-1][0])
        dp[i][1] = min(dp[i-2][1]+rock[i-2][1], dp[i-1][1]+rock[i-1][0], dp[i-3][0]+k)
    print(min(dp[n-1][0], dp[n-1][1]))    
    