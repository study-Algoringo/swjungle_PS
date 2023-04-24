def solution(priorities, location):
    answer = 0
    new_priorities = []
    for i in range(len(priorities)):
        new_priorities.append([priorities[i], i])
   
    while new_priorities:
                priority = new_priorities.pop(0)
                a,b = priority[0], priority[1]
                if not new_priorities:
                    answer += 1
                    break
                elif a >= max(new_priorities)[0]:
                    answer += 1
                    if b == location:
                        break
                else:
                    new_priorities.append(priority)
            
            
            
    return answer

print(solution([1, 1, 2, 3, 2, 1], 0))
