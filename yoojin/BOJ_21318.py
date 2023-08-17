import sys
read = sys.stdin.readline

n = int(read())
difficulty = list(map(int, read().split()))
prefix_sum = [0] * n

cnt = 0
for i in range(1, n):
    if difficulty[i - 1] > difficulty[i]:
        cnt += 1
    prefix_sum[i] = cnt

q = int(read())
for _ in range(q):
    x, y = map(int, read().split())
    print(prefix_sum[y - 1] - prefix_sum[x - 1])