from collections import deque

def solution(queue1, queue2):
    answer = 0
    # deque가 pop이 더 빠르므로 deque로 변환
    queue1 = deque(queue1); queue2 = deque(queue2)
    max_recursion = len(queue1) + len(queue2)
    q1_sum = sum(queue1); q2_sum = sum(queue2)
    
    while q1_sum != q2_sum:
        if answer > 3 * max_recursion:
            answer = -1
            break
        # 큐의 모든 원소의 합 구하기
        
        if q1_sum > q2_sum:
            pop_elem = queue1.popleft()
            queue2.append(pop_elem)
            q1_sum -= pop_elem
            q2_sum += pop_elem
        else:
            pop_elem = queue2.popleft()
            queue1.append(pop_elem)
            q1_sum += pop_elem
            q2_sum -= pop_elem
            
        answer += 1
        
    return answer