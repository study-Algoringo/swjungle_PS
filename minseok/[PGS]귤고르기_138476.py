from collections import Counter

def solution(k, tangerine):
    answer = 0
    box = Counter(tangerine).most_common()
    
    for i in range(len(box)):
        k -= box[i][1]
        answer += 1
        if k <= 0:
            break
    
    return answer