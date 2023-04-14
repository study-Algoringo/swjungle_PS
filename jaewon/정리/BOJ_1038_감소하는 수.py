import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())

result = []
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 9876543210까지여서 11까지 해줘야함
for i in range(1, 11):
	for j in combinations(arr, i):
		num = ''.join(list(map(str, reversed(list(j)))))
		result.append(int(num))

result.sort()
if n >= len(result):
	print(-1)
else:
	print(result[n])

# 풀이
# https://velog.io/@sugyeonghh/%EB%B0%B1%EC%A4%80-1038-%EA%B0%90%EC%86%8C%ED%95%98%EB%8A%94-%EC%88%98Python
