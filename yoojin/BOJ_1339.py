# import sys
# read = sys.stdin.readline

# chars = []; nums = [''] * 10
# n = int(read())
# sum = 0

# # 큰 자리 수에 큰 수를 배정
# for _ in range(n):
#     chars.append(read().rstrip())
# chars.sort(key=len, reverse=True)

# next_num = 9
# while len(chars[0]) != 0:
#     # 가장 긴 문장의 첫 번째 알파벳을 남은 숫자 중 가장 큰 수로 택하고 len 곱하기, sum에 더하기
#     if chars[0][0] not in nums:
#         while nums[next_num] != '':
#             next_num -= 1
#         nums[next_num] = chars[0][0]
#         sum += next_num * 10 ** (len(chars[0]) - 1)
#     else:
#         for i in range(next_num, 10):
#             if nums[i] == chars[0][0]:
#                 sum += i * 10 ** (len(chars[0]) - 1)
#     chars[0] = chars[0][1:]
#     # 길이를 key로 sort
#     chars.sort(key=len, reverse=True)
# print(sum)
import sys

chars = []
n = int(input())

for _ in range(n):
    chars.append(input().rstrip())

# 알파벳별로 자릿수 계산
char_values = {}
for char in chars:
    for i, c in enumerate(char[::-1]):
        if c not in char_values:
            char_values[c] = 0
        char_values[c] += 10 ** i

# 자릿수를 기준으로 내림차순 정렬
# dict를 정렬해야하기 때문에 items로 key, value 쌍 얻기
sorted_chars = sorted(char_values.items(), key=lambda x: x[1], reverse=True)

# 가장 큰 숫자부터 9부터 할당하면서 결과 계산
result = 0
current_digit = 9
for char, value in sorted_chars:
    result += current_digit * value
    current_digit -= 1

print(result)