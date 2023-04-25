# def solution(number, k):
#     real_list = []
#     answer = ''
#     num_list = [int(i) for i in number]
#     p =0
#     while k:
#         for j in range(p, len(num_list)-1):
#             if num_list[j] ==9:
#                 continue
            
#             elif num_list[j]<num_list[j+1]:
#                 num_list.pop(j)
#                 if j >50:
#                     p = j-10
#                 k -= 1
#                 break
            
#         else:
#             for _ in range(k):
#                 num_list.pop(-1)
#                 k -= 1
            
            
        
#     str_num = ''.join(map(str, num_list))

#     answer += str_num

    
    
#     return answer


def solution(number, k):
    stack = []
    for i, num in enumerate(number):
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        if k == 0:
            stack += list(number[i:])
            break
        stack.append(num)
    answer = ''.join(stack[:-k] if k > 0 else stack)
    return answer

print(solution("93939", 3))