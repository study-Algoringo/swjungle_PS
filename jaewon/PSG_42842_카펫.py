def solution(brown, yellow):
    answer = []
    # yellow가 하나일때는 무조건 brown이 9이다.
    if yellow == 1:
        answer.append(3)
        answer.append(3)
        return answer

    for j in range(1, yellow):
        if yellow % j == 0:
            yellow_h = j
            yellow_w = yellow // j
            brown_h = yellow_h + 2
            brown_w = yellow_w + 2
            # brown의 개수가 같고 answer가 비어있는경우만 => [8,6], [6,8] 들어오는걸 방지
            if brown == (brown_h - 2) * 2 + brown_w * 2 and len(answer) == 0:
                answer.append(brown_w)
                answer.append(brown_h)
    return answer