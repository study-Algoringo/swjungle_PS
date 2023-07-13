import sys
from itertools import combinations

read = sys.stdin.readline

while True:
    line = list(map(int, read().split()))
    k, nums = int(line[0]), line[1:]
    if k == 0:
        break
    
    for i in combinations(nums, 6):
        print(' '.join(map(str,i)))
    print()