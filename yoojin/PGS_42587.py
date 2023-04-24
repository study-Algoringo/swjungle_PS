from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([])
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    
    while q:
        temp = q.popleft()
        if len(q) == 0:
            answer += 1
            break
        elif temp[0] < max(q)[0]:
            q.append(temp)
        else:
            answer += 1
            if temp[1] == location:
                break
    return answer

    # [첫 시도] - 해당 인덱스가 다시 맨 끝에 가는 경우를 고려하지 못함
    # for i in range(location):
    #     temp = q.popleft()
    #     if temp != max(q):
    #         q.append(temp)
    # answer = len(priorities) - len(q) + 1 

print(solution([1, 1, 9, 1, 1, 1], 0))