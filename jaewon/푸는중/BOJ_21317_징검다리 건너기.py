import sys
sys.stdin=open("/Users/admin/Documents/swjungle_PS/jaewon/푸는중/input.txt", "rt")
input = sys.stdin.readline

N = int(input())
stone = []

# dp 배열(돌다리까지 오는데 필요한 최소 에너지 값을 저장하는 배열) 생성
dp = [1e9]*N
dp[0] = 0
for i in range(N-1):
    one, two = map(int, input().split())
    stone.append((one, two))
    if i+1<N : dp[i+1] = min(dp[i+1], dp[i]+one) # 현재 돌다리에서 다음 돌다리로 한 칸 이동하는 경우의 최소 에너지 값
    if i+2<N : dp[i+2] = min(dp[i+2], dp[i]+two) # 현재 돌다리에서 다음 돌다리로 두 칸 이동하는 경우의 최소 에너지 값

# 매우 큰 점프 적용해보며 최솟값 찾기
K = int(input())
_min = dp[-1]

# 점프를 할 경우 현재 위치에서 최소 3개 이상의 돌다리를 건너야 하므로, 인덱스를 3부터 시작
for i in range(3, N):
    # e는 현재 점프하는 위치에서의 최소 에너지 값
    e, dp1, dp2 = dp[i-3]+K, 1e9, 1e9

    # 현재 위치에서부터 마지막 돌다리까지 반복문
    for j in range(i, N-1):
        # dp1 현재 위치에서 다음 돌다리로 한 칸 이동하는 경우의 최소 에너지 값
        if i+1<=N : dp1 = min(dp1, e+stone[j][0])

        # dp2 현재 위치에서 다음 돌다리로 두 칸 이동하는 경우의 최소 에너지 값
        if i+2<=N : dp2 = min(dp2, e+stone[j][1])

        # 다음 위치로 넘어가기 전에 e는 다음 돌다리로 이동할 때 dp1과 dp2 중에서 
        # 더 작은 값을 갖습니다. dp1, dp2는 다음 위치에서 이전에 구한 값들과 
        # 현재 초기화된 매우 큰 값 중에서 더 작은 값을 갖습니다.
        e, dp1, dp2 = dp1, dp2, 1e9
    _min = min(_min, e)

print(_min)