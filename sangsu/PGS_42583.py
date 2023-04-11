from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    bridge=[0]*bridge_length
    answer=0
    truck_weights=deque(truck_weights)
    while bridge:
        
        bridge.pop(0)
        answer+=1
        if truck_weights:
            if sum(bridge)+truck_weights[0]<=weight:
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    return answer
