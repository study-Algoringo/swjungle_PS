def solution(clothes):
    answer = 1
    # 딕셔너리 쓰기
    clothe_table = {}
    for i in clothes:
        key = i[1]
        value = i[0]
        if key in clothe_table:
            clothe_table[key].append(value)
        else:
            clothe_table[key] = [value]
    for key in clothe_table.values():
