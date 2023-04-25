# 참고한 풀이
def solution(number, k):
    answer = [] # 스택 활용
    for n in number:
        while k > 0 and answer and answer[-1] < n:
            answer.pop()
            k -= 1
        answer.append(n)

    return ''.join(answer[:len(answer) - k])

# 실패한 풀이
# def solution(number, k):
#     n = list(number)
#     answer = ''
#     i = 0
#     while k > 0:
#         start = n[i]
#         end = n[i+1]
#         if start != end:
#             if (start < end):
#                 n.remove(start)
#                 k -= 1
#             else:
#                 n.remove(end)
#                 k -= 1
#         else:
#             i += 1
# 
#     return ''.join(n)

# 마지막 테스트 케이스 4177252841 결과값: 772841 기댓값: 775841
