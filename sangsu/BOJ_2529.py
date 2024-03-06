import sys
input = sys.stdin.readline
from itertools import permutations
n = int(input())
comparisons = list(map(str, input().split()))
max_num = 0
min_num = 0
for per in permutations(range(10), n+1):
    con = 0
    level = 0
    for i in range(n):
        if comparisons[i] == '<' and per[i] > per[i+1]:
            con = 1
            break
        elif comparisons[i] == '>' and per[i] < per[i+1]:
            con = 1
            break
        else:
            level += 1
            if level == n :
                per = list(per)
                min_num = "".join(map(str, per))
                
                brk =1
    if con:
        continue
    elif brk:
        break
    
number_list = list(permutations(range(10), n+1))
    
for per in reversed(number_list):
    con = 0
    level = 0
    brk = 0
    for i in range(n):
        if comparisons[i] == '<' and per[i] > per[i+1]:
            con = 1
            break
        elif comparisons[i] == '>' and per[i] < per[i+1]:
            con = 1
            break
        else:
            level += 1
            if level == n :
                per = list(per)
                max_num = "".join(map(str, per))
               
                brk =1
    if con:
        continue
    
    elif brk:
        break
    
print(max_num)
print(min_num)
                

