def solution(bridge_length, weight, truck_weights):
    answer = 0
    temp = [0]*bridge_length
    
    while temp:
        answer+=1
        temp.pop(0)
        
        if truck_weights:
            if sum(temp) + truck_weights[0] > weight:
                temp.append(0)
            else:
                temp.append(truck_weights.pop(0))
    return answer