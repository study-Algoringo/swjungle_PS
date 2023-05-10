n, h = map(int, input().split())

seok = [] # 석순
jong = [] # 종유석

# 첫번째가 석순 = 홀수
for i in range(n):
    if i % 2 == 0: # 짝수 = 종유석
        jong.append(int(input()))
    else:
        seok.append(int(input()))

seok.sort()
jong.sort()


# 이분 탐색
def search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


for i in range(1, h + 1):
    
