# 시간 초과
from itertools import combinations
def solution(number, k):
    # answer = ''
    result = 0
    answer = (list(map(list,(combinations(number,len(number)-k)))))
    for data in answer:
        result = max(result,int(''.join(data)))
        
    return str(result)

# 정답 보고한 것
def solution(number, k):
    stack = []

    for num in number:
        while stack and stack[-1] < num and k!=0:
            stack.pop()
            k-=1 
        stack.append(num)

    if k!=0:
        stack = stack[:-k]
    return ''.join(stack)


print(solution("4177252841",4))