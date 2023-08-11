import sys
from itertools import combinations
import math
read = sys.stdin.readline

n = int(read())
ground = [list(map(int, read().split())) for _ in range(n)]

# 모든 가능한 씨앗의 자리에 대해서 문제의 조건을 만족하는지 확인

# Solution 1
# 가능한 씨앗의 좌표를 모두 구해 놓고, combination 이용해 3개 뽑아서 각각의 비용을 계산
dots = []
for i in range(1, n-1):
    for j in range(1, n-1):
        dots.append((i, j))

def area(dots):
    a, b, c = dots
    # 만약 중복된 좌표가 존재한다면, 최소값에 포함하지 않도록
    if math.dist(a, b) <= 2 or math.dist(b, c) <= 2 or math.dist(a, c) <= 2:
        return 1e9
    return flower_area(a) + flower_area(b) + flower_area(c)

def flower_area(dot):
    ret = 0
    ret += ground[dot[0] - 1][dot[1]] + ground[dot[0] + 1][dot[1]] + ground[dot[0]][dot[1] - 1] + ground[dot[0]][dot[1] + 1] + ground[dot[0]][dot[1]]
    return ret

candidates = []; answer = 1e9
for combination in combinations(dots, 3):
    answer = min(answer, area(combination))
print(answer)