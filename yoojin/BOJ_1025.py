import sys
import math
read = sys.stdin.readline

# 해당 num이 제곱수인지 확인
def is_square(num):
    return math.pow(int(math.sqrt(num)), 2) == num

n, m = map(int, read().split())
arr = [list(map(int, read().rstrip())) for _ in range(n)]

result = -1

for i in range(n):
    for j in range(m):
        for dx in range(-n, n):
            for dy in range(-m, m):
                if dx == 0 and dy == 0:
                    continue

                x, y = i, j
                num = 0

                while 0 <= x < n and 0 <= y < m:
                    num = num * 10 + arr[x][y]
                    if is_square(num):
                        result = max(result, num)
                    x += dx
                    y += dy
print(result)