import sys
read = sys.stdin.readline

n, m, h = map(int, read().split())
lines = []

for _ in range(m):
    a, b = map(int, read().split())
    lines.append((a, b))
lines.sort()

# 사다리 타는 함수
def ladder(a, b):
    # 시작점을 기준으로, 다음 이동 세로선을 저장
    # 이동 가능한 세로선 : 가로선이 현재 가로선보다 크면서 같은 세로선을 가지는 경우
    # 이동 가능한 세로선이 없다면, 현재 세로선을 리턴한다.
    if (a, b + 1) in lines:
        return ladder(a, b + 1)
    elif (a, b - 1) in lines:
        return ladder(a, b - 1)
    else:
        return a + 1
print(ladder(1, 1))