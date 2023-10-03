# import sys
# read = sys.stdin.readline

# num = read().strip()
# m = int(read())
# broken_buttons = list(read().split())

# # num에 가장 가까운 번호 구하기
# answer = 0; current = 0

# for i, n in enumerate(num):
#     # 해당 자리수가 있으면 선택
#     # 해당 자리수가 없는 경우, 1씩 차이 나는 인접한 숫자부터
#     if n not in broken_buttons:
#         current += int(n) * (len(num) - i)
#     else:
#         k = 100
#         for j in range(0, 10):
#             if j == n:
#                 continue
#             if j not in broken_buttons:
#                 if abs(k - int(n)) > abs(int(n) - j):
#                     k = j
#         current += j * (len(num) - i)
#     answer += 1

# # 그 번호에서 -/+를 이용해서 목표 숫자 만들기
# answer += int(num) - current

# # 처음 num이 100인 경우
# if num == '100':
#     answer = 0
# print(answer)

import sys
read = sys.stdin.readline

target = int(read())
n = int(read())
broken_buttons = list(map(int, read().split()))

min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        if int(nums[j]) in broken_buttons:
            break
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)