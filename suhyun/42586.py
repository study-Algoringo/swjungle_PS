from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    nocomplete = deque()

    for i in range(len(speeds)):
        nocomplete.append(math.ceil((100-progresses[i])/speeds[i]))
    
    a = nocomplete.popleft()
    cnt = 1
    while nocomplete:
        if nocomplete[0] > a:
            answer.append(cnt)
            a = nocomplete.popleft()
            cnt=1
        else:
            nocomplete.popleft()
            cnt+=1
    answer.append(cnt) 
    return answer

print(solution([93, 30, 55],[1, 30, 5]))