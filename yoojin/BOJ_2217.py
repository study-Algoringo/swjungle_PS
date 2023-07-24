import sys
read = sys.stdin.readline

n = int(read())
weights = []; answer = 0

for _ in range(n):
    weight = int(read())
    weights.append(weight)
weights.sort()

for i in range(len(weights)):
    answer = max(answer, weights[i] * (n - i))

print(answer)