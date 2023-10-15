# import sys
# read = sys.stdin.readline

# # 문제 난이도의 합은 L보다 크거나 같고, R보다 작거나 같아야
# # 가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는 X보다 크거나 같

# n, l, r, x = map(int, read().split())
# difficulty = list(map(int, read().split()))

# # 2개 이상의 문제를 포함한 부분집합 중 조건을 만족하는 집합의 수
# def check(problem_set):
#     # l <= 합 <= r이고 차 >= x
#     return l <= sum(problem_set) <= r and (max(problem_set) - min(problem_set)) >= x

# def solution(problem_set, visited):
#     # 방문하지 않은 problem 추가
#     for problem in difficulty:
#         if problem not in visited:
#             visited.append(problem)
#     # check 후 조건 만족하지 않으면 return
#     if not check(problem_set):
#         return
#     # 조건 만족하면 다시 solution
#     else:
#         solution(problem_set)

from itertools import combinations

n, l, r, x = map(int, input().split())
difficulty = list(map(int, input().split()))
count = 0

for i in range(2, n + 1):
    difficulty_combination = list(combinations(difficulty, i))
    for j in difficulty_combination:
        if l <= sum(j) <= r and max(j) - min(j) >= x:
            count += 1

print(count)