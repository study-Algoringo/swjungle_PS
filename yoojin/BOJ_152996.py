def solution(weights):
    answer = 0
    dict = {}

    weights.sort()
    for i in weights:
        dict[i] = dict.get(i, 0)
        dict[i] += 1

    for i in dict:
        if (i * 3) % 2 == 0 and int(i * 3 / 2) in dict:
            answer += int(dict[i] * dict[int(i * 3 / 2)])
        if (i * 4) % 3 == 0 and int(i * 4 / 3) in dict:
            answer += int(dict[i] * dict[int(i * 4 / 3)])
        if i * 2 in dict:
            answer += int(dict[i] * dict[i * 2])
        answer += int(dict[i] * (dict[i] - 1) / 2)

    return answer