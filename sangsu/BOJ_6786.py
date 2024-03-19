import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
ans = 0
for nums in permutations(num_list, n):
    total = 0
    for i in range(n-1):
        total += abs(nums[i]- nums[i+1])
    
    if total >= ans:
        ans = total
        
print(ans)