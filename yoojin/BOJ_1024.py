import sys
read = sys.stdin.readline

n, l = map(int, read().split())

for length in range(l, 101):
    start = (2 * n - length * (length - 1)) / (2 * length)

    if start.is_integer() and start >= 0:
        start = int(start)
        sequence = list(range(start, start + length))
        print(*sequence)
        break
else:
    print(-1)