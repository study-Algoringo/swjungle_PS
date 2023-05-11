from collections import Counter
def solution(k, tangerine):
    answer = 0
    result = k
    data = list(zip(Counter(tangerine).keys(),Counter(tangerine).values()))
    data.sort(key=lambda x : -x[1])
    
    for k,v in data:     
        if result <= 0:
            break
            
        result-=v
        answer+=1


    return answer

print(solution(2,[1, 1, 1, 1, 2, 2, 2, 3]))