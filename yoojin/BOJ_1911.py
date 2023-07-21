import sys
read = sys.stdin.readline

n, l = map(int, read().split())
pool_list = []

for _ in range(n):
    start, end = map(int, read().split())
    pool_list.append((start, end))

# 널빤지 끝나는 지점 기억, 끝나는 지점이 웅덩이면 다시 +1
pool_list.sort()

pos = 0; count = 0
max_pos = max(map(max, pool_list))

for pool in pool_list:
    if pool[0] > pos:
        pos = pool[0]
    while pos in range(pool[0], pool[1]):
        pos += l
        count += 1
print(count)