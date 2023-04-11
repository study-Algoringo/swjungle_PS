def solution(numbers):
    numbers = list(map(str, numbers))
    # 람다 사용법 숙지하기 문자열 정렬!!!!
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

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

# 참고사이트
# https://jokerldg.github.io/algorithm/2021/05/06/most-big-number.html