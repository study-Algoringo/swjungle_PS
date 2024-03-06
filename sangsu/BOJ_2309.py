import sys
from itertools import combinations
input = sys.stdin.readline

nine_shorts = []
for _ in range(9):
    nine_shorts.append(int(input()))
    
nine_shorts.sort()
    
for seven_shorts in combinations(nine_shorts, 7):
    if sum(seven_shorts) == 100:
        for short in seven_shorts:
            print(short)
        break
    
    else:
        continue