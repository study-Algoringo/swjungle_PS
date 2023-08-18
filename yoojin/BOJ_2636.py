import sys
from collections import deque
read = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, read().split())
grid = list(list(map(int, read().split())) for _ in range(r))
cheeze = []

def melt():
    melting = deque([(0, 0)])
    check = [[False] * c for _ in range(r)]
    count = 0

    while melting:
        x, y = melting.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if grid[nx][ny] == 0 and check[nx][ny] == False:
                    check[nx][ny] = True
                    melting.append((nx, ny))
                elif grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    count += 1
                    check[nx][ny] = True
    return count

result = []
time = 0
while True:
    count = melt()
    result.append(count)
    if count == 0:
        break
    time += 1

print(time)
print(result[-2])