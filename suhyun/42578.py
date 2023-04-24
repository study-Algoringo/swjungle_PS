import sys
from itertools import product
def solution(clothes):
    answer = []
    result = 0
    min_len = sys.maxsize
    new_list = []
    type = {}
    for data in clothes:
        if data[1] not in type:
            type[data[1]] = []
        type[data[1]].append(data[0])
    
    for i in type.values():
        new_list.append(i)

    answer = list(product(*new_list))

    for c in type.values():
        result += len(c)

    return result + len(answer)

# 정답 코드
def solution(clothes):
    answer = 1
    type = {}
    for data in clothes:
        if data[1] not in type:
            type[data[1]] = []
        type[data[1]].append(data[0])
    
    for v in type.values():
        answer *= len(v)+1
    
    return answer-1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))