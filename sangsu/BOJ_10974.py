import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

num_list = permutations(range(1, n+1))

for num in num_list:
    num = map(str, num)
    print(" ".join(num))

    