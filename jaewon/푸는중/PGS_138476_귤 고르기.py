from collections import Counter

def solution(k, tangerine):
    answer = 0
    num_cnt = Counter(tangerine)
    cnt_list = sorted(num_cnt.values(), reverse=True)
    
    res = 0
    cnt = 0
    for c in cnt_list:
        res += c
        cnt += 1
        if res >= k:
            answer = cnt
            break

    return answer

# def solution(k, tangerine):
#     answer = 0
#     num_list = list(set(tangerine))
#     cnt_list = [0] * len(num_list)
#     for i in range(len(cnt_list)):
#         cnt_list[i] = tangerine.count(num_list[i])
    
#     res = 0
#     cnt = 0
#     for i in range(len(cnt_list)):
#         res += max(cnt_list)
#         cnt_list.remove(max(cnt_list))
#         cnt += 1
#         if res >= k:
#             answer = cnt
#             break

#     return answer

arr = [1, 3, 2, 5, 4, 5, 2, 3]

print(solution(6, arr))
