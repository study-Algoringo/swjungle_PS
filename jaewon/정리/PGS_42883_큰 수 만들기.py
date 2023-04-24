def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        # 제외할 수 k가 남아있고 answer이 비어있지 않으면서 answer에 있는 값보다 넣을 num이 크다면
        while k > 0 and answer and answer[-1] < num:
            # answer에서 하나를 제외하고 k -= 1를 한다.
            answer.pop()
            k -= 1
        # answer이 비었으면 일단 넣어준다.
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])


# print(solution("1924", 2))
# 기대값 : "94"
# print(solution("4177252841", 4))
# 기대값 : "775841"
print(solution("999", 2))
# 기대값 : 9