import sys
read = sys.stdin.readline

n = int(read())
warehouse = []; answer = 0

for _ in range(n):
    a, b = map(int, read().split())
    warehouse.append([a, b])

# 정렬하기
warehouse.sort()

max_height = max(warehouse, key = lambda x:x[1])
max_idx = warehouse.index(max_height)

h = warehouse[0][1]
left_warehouse = warehouse[:max_idx + 1]
right_warehouse = warehouse[max_idx:]

for i in range(max_idx):
    if h < left_warehouse[i + 1][1]:
        answer += h * (left_warehouse[i+1][0] - left_warehouse[i][0])
        h = left_warehouse[i+1][1]
    else:
        answer += h * (left_warehouse[i+1][0] - left_warehouse[i][0])

h = warehouse[-1][1]
for i in range(len(right_warehouse) - 1, 0, -1):
    if h < right_warehouse[i - 1][1]:
        answer += h * (right_warehouse[i][0] - right_warehouse[i-1][0])
        h = right_warehouse[i-1][1]
    else:
        answer += h * (right_warehouse[i][0] - right_warehouse[i-1][0])

answer += max_height[1]
print(answer)