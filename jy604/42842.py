def solution(brown, yellow):
    answer = []
    # brown * yellow = 전체 넓이
    total = brown + yellow
    # 높이를 3부터 시작, 오름차순으로 증가
    for h in range(3, total + 1):
        if total % h == 0:
            w = total / h
            if (w - 2) * (h - 2) == yellow:
                answer = [w, h]
                break
    return answer
