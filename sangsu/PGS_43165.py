from collections import deque
def solution(numbers, target):
    
    answer = 0
    que = deque()
    
    que.append((-numbers[0], 0))
    que.append((numbers[0], 0))
    while que:
        num, idx = que.popleft()
        if idx == len(numbers) -1 and num == target:
             answer += 1
             continue
         
        if idx == len(numbers) -1:
             continue 
            
        que.append((num -numbers[idx+1], idx+1))
        que.append((num +numbers[idx+1], idx+1))
            
        
    return answer


print(solution)






