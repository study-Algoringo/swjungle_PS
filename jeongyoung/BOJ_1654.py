import sys
k, n = map(int, sys.stdin.readline().split())
line = []
for _ in range(k):
    line.append(int(input()))
line.sort()
start = 1
end = line[-1]
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in line:
        total += (x // mid) # 랜선의 개수
    if n <= total: # 랜선이 분기점/ 자른 랜선이 필요한 랜선보다 크거나 같으면
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
