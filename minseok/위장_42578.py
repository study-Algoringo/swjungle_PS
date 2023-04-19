def solution(clothes):
    answer = 1
    cloth = {}
    
    for name, category in clothes:
        if category in cloth:
            cloth[category] += 1
        else:
            cloth[category] = 1

    for key, value in cloth.items():
        answer *= (value+1)
        
    return answer-1
