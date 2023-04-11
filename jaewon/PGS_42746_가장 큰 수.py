def solution(numbers):
    tmp = list(''.join(map(str, numbers)))
    tmp = list(map(int, tmp))
    tmp.sort(reverse=True)
    answer = ''.join(map(str, tmp))
    return answer

print(solution([3, 30, 34, 5, 9]))



# 풀었는데 시간초과....................................
# from itertools import permutations

# def solution(numbers):
#     res = []
#     per = list(permutations(numbers))
#     for num in per:
#         num = map(str, num)
#         res.append(int(''.join(num)))
#     answer = str(max(res))

#     return answer