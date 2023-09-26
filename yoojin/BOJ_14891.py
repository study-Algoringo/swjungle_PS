import sys
import collections
read = sys.stdin.readline

# 2번, -2번이 닿는 톱니
gear = []
for _ in range(4):
    gear.append(list(map(int, read().strip())))

def turn(n, dir):
    if dir == 1:
        gear[n].insert(0, gear[n].pop())
    elif dir == -1:
        gear[n].append(gear[n].pop(0))
        
    if n > 0 and gear[n][-2] != gear[n-1][2]:
        turn(n - 1, -dir)
    if n < 3 and gear[n][2] != gear[n+1][-2]:
        turn(n + 1, -dir)

n = int(read())
for _ in range(n):
    a, b = map(int, read().split())
    turn(a - 1, b)

score = 0
for i in range(4):
    score += gear[i][0] * (2 ** i)
print(score)