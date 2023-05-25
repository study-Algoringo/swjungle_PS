# 강의의 수. 블루레이 개수
n, m = map(int, input().split())
num = list(map(int, input().split()))

# start = 0
# mid = max(num)
# end = sum(num)

total = sum(num)
start = 0
end = 1e9
mid = 0
while start <= end:
    mid = (start + end) // 2

    if mid < max(num):
        start = mid + 1
        continue

    cnt = 1
    tmp = 0

    for i in range(n):
        if tmp + num[i] <= mid:
            tmp += num[i]
        else:
            tmp = num[i]
            cnt += 1

    if cnt <= m:
        end = mid - 1
        total = min(total, mid)
    else:
        start = mid + 1

print(int(total))
