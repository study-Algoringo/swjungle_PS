def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = [0]*bridge_length
    
    
    while truck:
        answer += 1
        truck.pop(0)                  
        if truck_weights:
            if sum(truck) + truck_weights[0] <= weight:
                truck.append(truck_weights.pop(0))
            else:
                truck.append(0)
        
    return answer

'''
# 시간초과 코드
# deque를 사용할 경우 시간 초과 발생
 
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = [0]*bridge_length
    
    truck_q = deque(truck)
    weight_q = deque(truck_weights)
    
    while truck_q:
        answer += 1
        truck_q.popleft()                
        if weight_q:
            if sum(truck_q) + weight_q[0] <= weight:
                truck_q.append(weight_q.popleft())
            else:
                truck_q.append(0)
        
    return answer
'''