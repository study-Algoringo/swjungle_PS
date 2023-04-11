# 민석 코드 참고
def solution(numbers):
    answer = ''
    numbers = sorted(numbers, reverse=True, key= lambda x: (str(x)*4)[0:4])
    # 6666 1010 2222 sort -> 6666 2222 1010 
    for i in numbers:
        answer += str(i) # 6210
    if answer[0] == "0": # 0일때 000으로 나와서 오류 발생
        answer = "0"
    return answer

# 시간 초과로 실패 뜬 답
# from itertools import permutations
# def solution(numbers):
#     answer = []
#     num = list(permutations(numbers, len(numbers)))
#     for i in num:
#         answer.append("".join(map(str, i)))
#     return max(answer)
