# def solution(people, limit):
#     answer = 0
#     people.sort()
#     n = len(people)
#     while people:
#         a = people.pop(0)
#         answer +=1
#         for b in reversed(people):
#             if a + b <= limit:
#                 people.remove(b)
#                 break
        
#     return answer

# print(solution([70, 50, 80, 50],100) )


def solution(people, limit):
    answer = 0
    people.sort()
    n = len(people)
    start = 0
    end = n-1

    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        
        end -= 1
        answer += 1
        

    return answer