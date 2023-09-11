import sys
read = sys.stdin.readline

n, l = map(int, read().split())

# 가운데 숫자를 기준으로 대칭 이루는 경우
for length in range(l, 101):
    start = (2 * n - length * (length - 1)) / (2 * length)

    if start.is_integer() and start >= 0:
        start = int(start)
        sequence = list(range(start, start + length))
# 좌우 대칭이 아닌 경우