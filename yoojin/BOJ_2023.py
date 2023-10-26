import sys
from math import sqrt
read = sys.stdin.readline

# Sol 1 - dp
# n자리의 신기한 소수는 (n - 1)자리의 신기한 소수 + 가능한 경우의 수 중 소수
n = int(read())
dp = [[] for _ in range(10)]
dp[1] = [2, 3, 5, 7]

# 소수 인지 확인
def is_prime(n):
    # 2부터 sqrt(n)까지 나누어 떨어지면 소수 x
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True

def solution1(n):
    # dp[n - 1]의 숫자들 내에서 가능한 모든 수를 소수 탐색
    for i in range(2, n + 1):
        for num in dp[i - 1]:
            for j in range(10):
                new_num = num * 10 + j
                if is_prime(new_num):
                    dp[i].append(new_num)

    for num in dp[n]:
        print(num)

# Sol 2 - 백트래킹 풀이
def solution2(current_num, num_digits, n):
    if num_digits == n:
        if is_prime(current_num):
            print(current_num)
        return
    
    for digit in range(10):
        new_num = current_num * 10 + digit
        if new_num != 0 and is_prime(new_num):
            solution2(new_num, num_digits + 1, n)
# for start_digit in [2, 3, 5, 7]:
#     solution2(start_digit, 1, n)
solution1(n)