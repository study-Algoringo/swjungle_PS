from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck = [0]*bridge_length
    
    truck[-1]=truck_weight[0]
    q = deque(truck)
    
    while q != [0]*bridge_length:
        deque.rotate(-1)
        answer += 1
        if 

    return answer
