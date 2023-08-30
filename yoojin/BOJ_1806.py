import sys
from collections import deque
read = sys.stdin.readline

n, s = map(int, read().split())
prefix_sum = []

# 누적합 구한 후
partial_sum = 0
prefix_sum.append(partial_sum)
for i in list(map(int, read().split())):
    partial_sum += i
    prefix_sum.append(partial_sum)

answer = 1000001
start = 0
end = 1

while start != n:
    if prefix_sum[end] - prefix_sum[start] >= s:
        if end - start < answer:
            answer = end - start
        start += 1
    else:
        if end != n:
            end += 1
        else:
            start += 1

if answer != 1000001:
    print(answer)
else:
    print(0)