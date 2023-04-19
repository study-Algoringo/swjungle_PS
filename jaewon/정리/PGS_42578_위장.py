def solution(clothes):
    answer = 1
    dic = {}

    for name, category in clothes:
        if category in dic:
            dic[category] += 1
        else:
            dic[category] = 1

    for key, value in dic.items():
        # 각 카테고리별로 옷의 개수를 담은 이후
        # 옷을 안입은 경우(value + 1)를 포함하여 경우의 수 계산
        # 결과값에서 1을 빼면 옷을 전부 안입은 경우를 제외하므로 경우의 수 산출 가능
        answer *= (value + 1)
    
    return answer - 1

tmp1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

solution(tmp1)