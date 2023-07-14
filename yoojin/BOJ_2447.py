import sys
read = sys.stdin.readline

n = int(read())
stars = [[' ' for _ in range(n)] for _ in range(n)]

def recursion(size, x, y):
    if size == 1:
        stars[y][x] = '*'
    else:
        next_size = size // 3
        for dy in range(3):
            for dx in range(3):
                if dy != 1 or dx != 1:
                    recursion(next_size, x + dx * next_size, y + dy * next_size)

recursion(n, 0, 0)
for star in stars:
    print(''.join(star))