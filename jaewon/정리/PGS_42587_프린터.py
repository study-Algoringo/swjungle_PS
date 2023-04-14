def solution(priorities, location):
    answer = 0
    new_priorities = []
    # 우선순위를 넣은 리스트와 함께 숫자를 리스트로 묶어서 append
    for i in range(len(priorities)):
        new_priorities.append([priorities[i], i])

    while new_priorities:
        a, b = new_priorities.pop(0)
        if not new_priorities:
            answer += 1
            break
        elif a >= max(new_priorities)[0]:
            answer += 1
            if b == location:
                break
        else:
            new_priorities.append([a, b])

    return answer

# solution([2, 1, 3, 2], 2)
solution([1, 1, 9, 1, 1, 1], 0)