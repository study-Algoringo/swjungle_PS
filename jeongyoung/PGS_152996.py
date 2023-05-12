# 탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같다면 시소 짝꿍
from collections import Counter

def solution(weights):
    answer = 0
    pair_cnt = Counter(weights)
    # 1:1 비율 구하기
    for i, j in pair_cnt.items():
        if j >= 2:
            # 중복 허용 - nC2
            answer += j * (j - 1) // 2
    weights = set(weights)
    
    for w in weights:
        if w * 2/3 in weights:
            answer += pair_cnt[w * 2/3] * pair_cnt[w]
        if w * 2/4 in weights:
            answer += pair_cnt[w * 2/4] * pair_cnt[w]
        if w * 3/4 in weights:
            answer += pair_cnt[w * 3/4] * pair_cnt[w]
    return answer
