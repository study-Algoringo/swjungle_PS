from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):

    target=[0,1,2,3,4,5,6,7,8,9,10]

    max_score_diff = 0
    max_comb = {}
    for comb in combinations_with_replacement(target, n):
        arrow=Counter(comb)
        ryan, peach = 0, 0
        for i in range(11):
            if info[10-i] < arrow[i]:
                ryan += i
            elif info[10-i] > 0:
                peach += i
        score_diff = ryan - peach
        if score_diff > max_score_diff:
            max_comb = arrow
            max_score_diff = score_diff
            
    if max_score_diff>0:
        answer=[0]*11
        for n in max_comb:
            answer[10-n] = max_comb[n]
        return answer
    else: 
        return [-1]
