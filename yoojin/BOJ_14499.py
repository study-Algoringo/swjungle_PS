import sys
read = sys.stdin.readline

n, m, x, y, k = map(int, read().split())
directions = []
dice = [0] * 7

for _ in range(n):
    directions.append(list(map(int, read().split())))

dir = list(map(int, read().split()))

# 처음 주사위의 [6]좌표가 바닥에 닿아 있음
# 다음에 닿는 주사위느 