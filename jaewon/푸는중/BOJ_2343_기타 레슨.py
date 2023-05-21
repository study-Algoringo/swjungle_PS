import sys
sys.stdin=open("/Users/admin/Documents/swjungle_PS/jaewon/푸는중/input.txt", "rt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 초기화
start = max(arr) # 블루레이 크기의 최솟값
end = sum(arr) # 블루레이 크기의 최댓값
res = 0

while start <= end:
    mid = (start + end) // 2
    count = 1  # 블루레이 개수
    total = 0  # 현재 블루레이에 저장된 강의 시간의 합

    for x in arr:
        if total + x > mid:  # 현재 블루레이에 강의를 녹화할 수 없으면
            count += 1 # 새로운 블루레이에 녹화
            total = x
        else:
            total += x

    if count <= m:  # 블루레이 개수가 m 이하이면
        res = mid
        end = mid - 1
    else: # 블루레이 개수가 m보다 큰 경우
        start = mid + 1

print(res)







