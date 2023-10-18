import sys
read = sys.stdin.readline

n = int(read())
house = []; dp = [0] * n

for _ in range(n):
    house.append(list(map(int, read().split())))

# n번째 최소 비용 -> n - 1번째 최소 비용 + n번째 집에 칠할 수 있는 색 중 최소 값