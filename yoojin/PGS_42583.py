from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque([]); answer = 0
    for truck in truck_weights:
        # queue에 푸시할 때마다 시간 1씩 증가
        sum = 0
        for i in queue:
            sum += i[0]
        if sum + truck <= weight:
            answer = answer + 1
            queue.append((truck, answer))
        # 더 넣을 수 없는 경우 맨 앞 원소를 팝하고 시간 = 해당 원소를 넣었던 시간 + 다리 길이로
        else:
            while sum + truck > weight:
                tmp = queue.popleft()
                answer = tmp[1] + bridge_length
                if len(queue) != 0 and queue[-1][1] >= answer:
                    answer = queue[-1][1] + 1
                sum -= tmp[0]
            
            queue.append((truck, answer))
        # pop할 때마다 현재 다리에 다른 트럭을 올릴 수 있는지 확인하기 (현재 무게와 다음에 올릴 트럭의 합이 최대 무게 미만인지 확인)
    # queue에 남은 트럭 처리
    if len(queue) != 0:
        answer = queue[-1][1] + bridge_length
    
    return answer
print(solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]))