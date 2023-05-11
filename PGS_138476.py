# 담으려는 수 k
def solution(k, tangerine):
    answer = []
    tangerine.sort()
    # 크기 중복 귤 구하기
    box = {}
    for i in tangerine:
        if i in box:
            box[i] += 1
        else:
            box[i] = 1
            
    # 재정렬
    for k in box.keys():
        answer.append(box[k])
    answer = sorted(answer)
    
   # count 
    cnt = 0
    while k > 0:
        k -= answer.pop()
        cnt += 1
    return cnt


# 1, 3, 2, 5, 4, 5, 2, 3
# 1, [2, 2], [3, 3], 4, [5, 5]
# 1, 4, [2, 2], [3, 3], [5, 5]
# 4개 뽑음 -> 1, 4, 2, 2
# 테스트 2 기댓값 2 결괏값 3 fail
