import sys
read = sys.stdin.readline

n = int(read())
# lines = []; answer = 0

# for i in range(n):
#     a, b = map(int, read().split())
#     lines.append([a, b, 0])

# def check_meetpoint(arr):
#     arr.sort(key=lambda x: x[0])
#     # line이 겹치는지 확인하고, 겹친다면 1 증가시킴
#     for i in range(len(arr)):
#         arr[i][2] = 0
#         for j in range(i + 1, len(arr)):
#             if arr[i][1] >= arr[j][1]:
#                 arr[i][2] += 1
#                 arr[j][2] += 1
#     arr.sort(key=lambda x: x[2], reverse=True)

# check_meetpoint(lines)
# # while 겹치는 line이 없을 때까지 반복
# while lines[0][2] != 0:
#     # 교점이 가장 많은 line을 먼저 제거
#     lines.pop(0)
#     answer += 1
#     # 모든 line에 대한 교점 개수 갱신
#     check_meetpoint(lines)

# print(answer)

lines = sorted([list(map(int, read().split())) for _ in range(n)])
dp = [1 for _ in range(n)]
# 최장 부분 수열을 찾고 그 값을 n에서 빼기
for i in range(n):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))