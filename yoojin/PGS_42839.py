from math import sqrt
from itertools import permutations

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0; nums = []; num_set = []
    # numbers를 n개의 숫자로 쪼개기
    for num in numbers:
        nums.append(int(num))

    # 숫자의 조합을 만들고, 그 숫자가 prime인지만 확인
    for i in range(1, len(nums) + 1):
        for j in permutations(nums, i):
            num_str = ''.join(map(str, j))
            num = int(num_str)
            num_set.append(num)
    num_set = set(num_set)

    for num in num_set:
        print(num)
        if(is_prime(num)):
            answer += 1

    return answer
