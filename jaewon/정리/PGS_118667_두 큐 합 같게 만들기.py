from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    total_sum = sum(queue1) + sum(queue2)
    cnt = 0
    answer = 0

    if total_sum % 2 != 0:
        return -1
    
    que_sum_one = sum(queue1)
    que_sum_two = sum(queue2)
    
    while True:
        if cnt > (len(queue1) + len(queue2)) * 2 or len(queue1) == 0 or len(queue2) == 0:
            return -1

        if que_sum_one < que_sum_two:
            tmp = queue2.popleft()
            queue1.append(tmp)
            cnt += 1
            que_sum_one += tmp
            que_sum_two -= tmp

        elif que_sum_one > que_sum_two:
            tmp = queue1.popleft()
            queue2.append(tmp)
            cnt += 1
            que_sum_one -= tmp
            que_sum_two += tmp
        else:
            answer = cnt
            break

    return answer

queue1 = [1, 1]
queue2 = [1, 5]

solution(queue1, queue2)