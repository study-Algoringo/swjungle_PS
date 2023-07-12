import sys
from itertools import permutations
read = sys.stdin.readline

n = int(read())
p = permutations(range(1, n+1), n)

for i in p:
    print(' '.join(map(str, i)))