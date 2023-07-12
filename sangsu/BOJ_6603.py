import sys
from itertools import combinations
input = sys.stdin.readline



while (1):
    num_list = list(map(int, input().split()))
    if len(num_list) == 1:
        break
    
    else:
        
        n = num_list.pop(0)
        com_list = combinations(num_list, 6)
        for com in com_list:
            numbers = map(str, com)
            print(" ".join(numbers))
    print()