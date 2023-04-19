def solution(clothes):
    # 딕셔너리 사용
    # headgear = [yellow_hat, green_turban]
    # eyegear = [blue_sunglasses]
    # 안입은 것, 1번 입은 것, 2번 입은 것 = 3 * 2 - 모든 안 입은 경우 제외(1) = 5
    clothe_table = {}
    answer = 1
    for i in clothes:
        key = i[1]
        value = i[0]
        if key in clothe_table:
            clothe_table[key].append(value)
        else:
            clothe_table[key] = [value]
    for key in clothe_table.values():
        answer *= len(key) + 1
    return answer - 1
