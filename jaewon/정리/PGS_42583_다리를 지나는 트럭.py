def solution(bridge_length, weight, truck_weights):
    # 경과시간, 다리 길이와 같은 길이의 값이 0으로 된 리스트
    answer = 0
    bridge = [0 for _ in range(bridge_length)]

    # 배열의 값을 빼면서 반복문을 실행
    while bridge:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)
    return answer

# 길이, 무게, 트럭무게
solution(2, 10, [7, 4, 5, 6])