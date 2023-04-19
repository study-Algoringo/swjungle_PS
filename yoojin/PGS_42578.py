def solution(clothes):
    answer = 1; dict = {}
    for name, type in clothes:
        if type in dict:
            dict[type] += 1
        else:
            dict[type] = 1
    for val in dict.values():
        answer *= (val + 1)
    
    return answer - 1