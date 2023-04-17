from itertools import permutations
# 소수를 판별하는 함수 만들기
def sosu(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    num = []
    result = []
    for i in range(1, len(numbers) + 1):
        # for i in permutations(numbers, i):
        num.extend(permutations(numbers, i))
        result = [int(''.join(i)) for i in num]

    for i in set(result):
        if sosu(i):
            answer += 1

    return answer

