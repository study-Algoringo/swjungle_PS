import sys
from itertools import combinations
read = sys.stdin.readline

n = int(read())
team = list(i for i in range(1, n + 1))
ability = [list(map(int, read().split())) for _ in range(n)]
answer = 1e9

def score(team):
    score = 0
    for i in team:
        # 모든 번호에 대해 score 더하기
        for j in team:
            score += ability[i - 1][j - 1]
    return score

# Solution 1 - 조합
# n개 중 최소 하나의 인원을 뽑아야 함
# combinations(team, 1) to combinations(team, n/2 + 1)
for i in range(1, int(n/2) + 1):
    for combi in combinations(team, i):
        rest_combi = [x for x in team if x not in combi]
        answer = min(answer, abs(score(combi) - score(rest_combi)))
print(answer)
# Solution 2 - dfs