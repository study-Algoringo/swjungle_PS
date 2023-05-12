# def solution(weights):
#     answer = 0
#     weights.sort()
#     n = len(weights)
#     for i in range(n):
#         for j in range(i+1, n):
#             if weights[j]/weights[i] == 1 or weights[j]/weights[i] == 3/2 or weights[j]/weights[i] == 4/3 or weights[j]/weights[i] == 2:
#                 answer += 1
        
#     return answer

# print(solution([100,180,360,100,270]))




from collections import Counter

def solution(weights):
    answer = 0
    count = Counter(weights)
    for k, v in count.items():
        if v > 1: answer += v * (v-1) / 2
    weights = list(set(weights))
    check = (3/4, 2/3, 1/2)
    for w in weights:
        for c in check:
            if w*c in weights:
                answer += count[w] * count[w*c]
    return answer