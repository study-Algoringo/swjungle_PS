import sys
read = sys.stdin.readline

n, k = map(int, read().split())

count = 0
while bin(n).count('1') > k:
    n = n + 1
    count = count + 1

print(count)

# n, k = map(int, read().split())

# # k + 1번째 자리부터 끝까지 0과 1을 반전시킨 후 1을 더하기
# b = format(n, 'b')

# for i in range(len(b)):
#     if b[i] == '1':
#         k -= 1
#         if k == 0:
#             b = b[i + 1:]
#             print(2 ** len(b) - int(b, 2))
#             break