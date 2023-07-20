# [BOJ] 색종이 올려 놓기 / Gold 4 / 2643 / 박정영
# 조건 1 : 새로 올라오는 생족이는 맨 위보다 크지 않아야함 new < old
# 조건 2 : 새로 올라오는 종이와 맨 위의 색종이 변들은 서로 평행한다 (색종이는 90도씩 돌릴 수 있다)
# 색종이는 두 변의 길이로 표현

n = int(input()) # 색종이 수
paper = []

for _ in range(n):
    width = list(map(int, input().split()))
    paper.append(sorted(width))

paper.sort()

dp = [1 for _ in range(n)] # 가장 긴 증가하는 부분 수열

for i in range(n):
    for j in range(i):
        if paper[i][1] >= paper[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
# for i in range(n):
#     w, h = map(int, input().split())
#     page.append()
#
# a = [1 for i in range(n)]
# print(dp)
# dp.sort(key=lambda x:x[0])
# print(dp)
# print(a)
#
# for i in range(1, n):
#     for j in range(i):
#         if
