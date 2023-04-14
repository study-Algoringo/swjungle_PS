# def solution(people, limit):
#     answer = 1
#     flag = 0
#     temp = [people[0]]
#     for i in range(1,len(people)):
#         for j in range(len(temp)):
#             if temp[j] + people[i] <= limit:
#                 temp[j] += people[i]
#                 flag = 1
#                 break
        
#         if flag!=1:
#             answer+=1
#             temp.append(people[i])

#     return answer

# 냅색은 이분법으로도 풀 수 있다.
from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    temp = deque(people)
    while temp:
        if len(temp) == 1:
            answer+=1
            break

        a = temp.popleft()
        b = temp.pop()

        if a+b > limit:
            answer+=1
            temp.append(0,a)
            temp.sort()
            continue

        answer+=1

    return answer


print(solution([70, 50, 80,50],100))