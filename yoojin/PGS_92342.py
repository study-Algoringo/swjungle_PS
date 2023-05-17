from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_gap = -1

    for combi in combinations_with_replacement(range(11), n):
        lion_info = [0] * 11

        for i in combi:
            lion_info[i] += 1
        
        appeach, lion = 0, 0
        for idx in range(11):
            if info[idx] == lion_info[idx] == 0:
                continue
            elif info[idx] >= lion_info[idx]:
                appeach += 10 - idx
            else:
                lion += 10 - idx
        
        if lion > appeach:
            gap = lion - appeach
            if gap > max_gap:
                max_gap = gap
                answer = lion_info
    return answer