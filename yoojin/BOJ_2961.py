import sys
from itertools import combinations
read = sys.stdin.readline

n = int(read())
ingredients = []
answer = 1e9

for _ in range(n):
    ingredients.append(list(map(int, read().split())))

# 모든 재료의 조합을 구해서 가장 작은 경우를 answer로
for i in range(1, n + 1):
    for combi in combinations(ingredients, i):
        sour = 1
        bitter = 0
        for c in combi:
            sour *= c[0]
            bitter += c[1]
        answer = min(answer, abs(sour - bitter))

print(answer)