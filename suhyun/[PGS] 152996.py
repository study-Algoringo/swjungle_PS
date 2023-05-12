# 시간 초과
# from itertools import combinations
# def solution(weights):
#     answer = 0
#     for x,y in combinations(weights,2):
#         if x*4 == y*2 or x*2 == y*4:
#             answer+=1
#         elif x*3 == y*2 or x*2 == y*3:
#             answer+=1
#         elif x*4 == y*3 or x*3 == y*4:
#             answer+=1
#         elif x == y:
#             answer+=1
#         else:
#             continue
#     return answer

# 정영언니 코드 이해
from collections import Counter
def solution(weights):
    result = 0
    answer = Counter(weights)
    temp = set(weights)

    for w in temp:
        if answer[w] > 1:
            result += answer[w] * (answer[w]-1) // 2
    
    for x in temp:
        if x * (2/4) in weights:
            result += answer[x]*answer[x*(2/4)]
        if x * (2/3) in weights:
            result += answer[x]*answer[x*(2/3)]
        if x * (3/4) in weights:
            result += answer[x]*answer[x*(3/4)]
    return result
    
print(solution([100,180,360,100,270]))
