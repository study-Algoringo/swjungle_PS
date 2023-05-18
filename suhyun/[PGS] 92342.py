from itertools import combinations_with_replacement
def solution(n, info):
    answer = []        
    for i in combinations_with_replacement([1,2,3],2):
        print(i)
    return answer

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))