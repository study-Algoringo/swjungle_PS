# 정답보고 진행
import sys ,copy
# 돌의 갯수
N = int(sys.stdin.readline())

# 작은 돌, 큰 돌 순서로 삽입
doll = [list(map(int,sys.stdin.readline().split())) for _ in range(N-1)]

# 매우 큰 돌일 경우 에너지 사용
K = int(sys.stdin.readline())

# 돌이 1개인 경우
if N == 1:
    print(0)
    exit()

# 돌이 2개인 경우
elif N == 2:
    print(doll[0][0])
    exit()

# 돌이 3개 이상인 경우
DP1 = [0] * (N)
result = []
DP1[1] = doll[0][0]

## (1) 작은 + 큰 점프만 고려했을 때의 결과
for i in range(2,N):
    DP1[i] = min(DP1[i-1]+doll[i-1][0],DP1[i-2]+doll[i-2][1])
result.append(DP1[N-1])

## (2) 작은 + 큰 점프 + 매우 큰 점프만 고려했을 때의 결과
DP2 = copy.deepcopy(DP1)
for j in range(N-3):
    DP2[j+3] = DP1[j] + K
    for i in range(j+4,N):
        DP2[i] = min(DP2[i-1]+doll[i-1][0],DP2[i-2]+doll[i-2][1])     
    result.append(DP2[N-1])
    
# 가능한 모든 경우의 수 중 최솟값 출력
print(min(result))
