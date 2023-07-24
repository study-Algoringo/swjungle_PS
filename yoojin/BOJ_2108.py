import sys
import math
read = sys.stdin.readline

t = int(read())

for i in range(t):
    a, b = map(int, read().split())
    print(math.comb(max(a, b), min(a, b)))