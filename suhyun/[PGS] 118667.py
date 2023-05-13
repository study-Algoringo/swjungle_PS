from collections import deque
def solution(queue1, queue2):
    answer = 0
    temp1 = deque(queue1)
    temp2 = deque(queue2)
    
    x = sum(queue1)
    y = sum(queue2)

    while x != y:
        if len(temp1) + len(temp2) < answer:
            return -1
        if x < y:
            a = temp2.popleft()
            temp1.append(a)
            x +=a
            y -=a 
            answer+=1
        else:
            b = temp1.popleft()
            temp2.append(b)
            x -= b
            y += b
            answer+=1

    return answer

print(solution([1,1],[1, 5]))