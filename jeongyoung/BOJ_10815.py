# 숫자 카드 10815
n = int(input())
ans = list(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))
ans.sort()


def search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for k in range(m):
    if search(ans, cards[k], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
