def solution(numbers):
    numbers = list(map(str, numbers))
    # 람다 사용법 숙지하기 문자열 정렬!!!!
    # 예를 들어, numbers 리스트의 요소가 ['3', '30', '34'] 이면 lambda x: x * 3 함수를 적용하면, 
    # '3' 은 '333', '30' 은 '303030', '34' 는 '343434' 로 변환됩니다. 이렇게 변환된 문자열들을 기준으로 정렬하면, 
    # 각 숫자들의 자릿수를 맞춰 정렬할 수 있습니다. 예를 들어, '333' 은 '303030' 보다 크며, '343434' 는 '303030' 보다 크고, 
    # '343434' 는 '333' 보다 크기 때문에, 최종적으로 정렬된 리스트는 [34, 3, 30] 이 됩니다.
    # 즉, 34/3/30, 34/30/4, 3/34/30, 3/30/34, 30/3/34, 30/34/3이 나올수있는데 그중 가장 큰 값을 보면 34330임을 확인할수 있다.
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